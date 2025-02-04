

//finalizar tarea boton
function quitarDeProcesos(tareaId) {
  if (confirm("¿Está seguro de que desea quitar esta tarea de los procesos y marcarla como finalizada?")) {
      finalizarTarea(tareaId);
  }
}

function finalizarTarea(tareaId) {
  fetch('/actualizar_tarea/', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken') // Asegúrate de que esta función esté definida para manejar CSRF tokens
      },
      body: JSON.stringify({
          id: tareaId,
          estado: 'finalizado',  // Cambiamos el estado a finalizado
      })
  })
  .then(response => response.json())
  .then(data => {
      if (data.success) {
          alert("La tarea se ha marcado como finalizada.");
          location.reload(); // Recargar la página para reflejar los cambios
      } else {
          alert("Error al actualizar la tarea: " + data.error);
      }
  })
  .catch(error => {
      console.error("Error:", error);
  });
}

//filtrar en busqueda  para actualizar en tiempo real "observaciones "______________________________________________

//filtrar en busqueda  para actualizar en tiempo real "descripcion "______________________________________________
document.addEventListener("DOMContentLoaded", function () {
  // Capturar clic en el botón de actualizar
  document.querySelectorAll(".btn-actualizar").forEach(button => {
      button.addEventListener("click", function () {
          const tareaId = this.getAttribute("data-id");
          const nuevaDescripcion = this.closest("tr").querySelector(".descripcion-input").value;

          // Enviar la nueva descripción al servidor
          fetch(`/actualizar_tarea_descripcion/`, {
              method: "POST",
              headers: {
                  "Content-Type": "application/json",
                  "X-CSRFToken": "{{ csrf_token }}" // Incluye el token CSRF
              },
              body: JSON.stringify({
                  id: tareaId,
                  descripcion: nuevaDescripcion
              })
          })
          .then(response => response.json())
          .then(data => {
              if (data.status === "success") {
                  mostrarModal("Éxito", "Descripción actualizada correctamente.");
              } else {
                  mostrarModal("Error", data.message || "Hubo un problema al actualizar la descripción.");
              }
          })
          .catch(error => {
              console.error(error);
              mostrarModal("Error", "Hubo un problema al actualizar la descripción.");
          });
      });
  });

  // Función para mostrar el modal con el mensaje
  function mostrarModal(titulo, mensaje) {
      const modalHTML = `
          <div class="modal fade" id="messageModal" tabindex="-1" aria-labelledby="messageModalLabel" aria-hidden="true">
              <div class="modal-dialog">
                  <div class="modal-content">
                      <div class="modal-header">
                          <h5 class="modal-title" id="messageModalLabel">${titulo}</h5>
                          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                      </div>
                      <div class="modal-body">
                          <p>${mensaje}</p>
                      </div>
                      <div class="modal-footer">
                          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
                      </div>
                  </div>
              </div>
          </div>
      `;
      document.body.insertAdjacentHTML('beforeend', modalHTML);
      const modal = new bootstrap.Modal(document.getElementById('messageModal'));
      modal.show();
  }
});

//filtrar en busqueda______________________________________________
function filterTable() {
  // Obtener el valor del input de búsqueda
  var input = document.getElementById('searchInput');
  var filter = input.value.toLowerCase(); // Convertir a minúsculas
  var table = document.getElementById('tareaAsignadaTableBody');
  var tr = table.getElementsByTagName('tr');

  // Iterar sobre las filas de la tabla
  for (var i = 0; i < tr.length; i++) {
      var td = tr[i].getElementsByTagName('td');
      var found = false;

      // Iterar sobre las celdas en cada fila
      for (var j = 0; j < td.length; j++) {
          if (td[j]) {
              var txtValue = td[j].textContent || td[j].innerText;
              if (txtValue.toLowerCase().indexOf(filter) > -1) {
                  found = true; // Si se encuentra el texto en alguna celda
                  break;
              }
          }
      }

      // Mostrar o ocultar la fila según el resultado de búsqueda
      tr[i].style.display = found ? "" : "none";
  }
}


//asignar tarea____________________________________________


function modificarAsignacion(tareaId) {
  const usuarioId = document.getElementById(`usuario-modificar-${tareaId}`).value;
  const csrftoken = getCookie('csrftoken');  // Obtenemos el token CSRF de las cookies

  if (usuarioId) {
      fetch(`/modificar_asignacion/${tareaId}/`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': csrftoken  // Incluimos el token CSRF en los headers
          },
          body: JSON.stringify({ usuario_id: usuarioId })
      })
      .then(response => {
          if (response.ok) {
              location.reload();  // Recargar la página después de modificar
          } else {
              console.error('Error al modificar la asignación.');
          }
      })
      .catch(error => console.error('Error:', error));
  }
}




// Función para obtener el CSRF token (debe estar incluida en tu main.js)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Comprueba si este cookie comienza con el nombre que buscamos
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


//-----------------------------




function cambiarAsignacion(tareaId) {
    const selectElement = document.getElementById(`usuario-select-asignado-${tareaId}`);
    const usuarioId = selectElement.value;

    // Hacer una solicitud AJAX para cambiar la asignación
    fetch(`/cambiar_asignacion/${tareaId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Asegúrate de tener la función getCookie definida
        },
        body: JSON.stringify({ usuario_id: usuarioId }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Asignación actualizada correctamente.');
            location.reload(); // Recarga la página para ver los cambios
        } else {
            alert('Error al actualizar la asignación.');
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// Función para obtener el CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Comprobar si esta cookie comienza con el nombre dado
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}




//---------------









//asignar tareas cambiando el id del usuario asignado______________________________

function asignarTarea(tabla, tareaId) {
  const usuarioSelectId = `${tabla}-usuario-select-${tareaId}`;
  const usuarioId = document.getElementById(usuarioSelectId).value;

  if (!usuarioId) {
      alert("Seleccione un usuario para asignar la tarea.");
      return;
  }

  fetch(`/asignar_tarea/${tareaId}/`, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken') // Asegúrate de enviar el token CSRF.
      },
      body: JSON.stringify({ usuario_id: usuarioId })
  })
  .then(response => response.json())
  .then(data => {
      if (data.success) {
          alert('Tarea asignada correctamente.');
          location.reload(); // Recargar la página para que se actualice el estado de las tareas.
      } else {
          alert('Error al asignar la tarea.');
      }
  });
}


function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

//codigo para ver tablas en asignar
 // Función para buscar tareas
 document.addEventListener("DOMContentLoaded", function() {
  const searchInput = document.getElementById('searchInput');
  const tareaTableBody = document.getElementById('tareaTableBody');

  searchInput.addEventListener('keyup', function() {
      const filter = searchInput.value.toLowerCase();
      const rows = tareaTableBody.getElementsByTagName('tr');

      Array.from(rows).forEach(row => {
          const cells = row.getElementsByTagName('td');
          let match = false;

          for (let i = 0; i < cells.length; i++) {
              if (cells[i].innerText.toLowerCase().includes(filter)) {
                  match = true;
                  break;
              }
          }

          row.style.display = match ? '' : 'none'; // Muestra u oculta la fila
      });
  });
});

document.addEventListener("DOMContentLoaded", function() {
  const searchInput1 = document.getElementById('searchInput1');
  const tareaTableBody = document.getElementById('tareaAsignadaTableBody'); // Corregido el ID

  searchInput1.addEventListener('keyup', function() {
      const filter = searchInput1.value.toLowerCase();
      const rows = tareaTableBody.getElementsByTagName('tr');

      Array.from(rows).forEach(row => {
          const cells = row.getElementsByTagName('td');
          let match = false;

          for (let i = 0; i < cells.length; i++) {
              if (cells[i].innerText.toLowerCase().includes(filter)) {
                  match = true;
                  break;
              }
          }

          row.style.display = match ? '' : 'none'; // Muestra u oculta la fila
      });
  });
});









//busqueda de tabla usuarios /admin
document.addEventListener("DOMContentLoaded", function() {
  // Obtiene el campo de búsqueda y la tabla
  const searchInput = document.getElementById("searchInput");
  const userTable = document.getElementById("userTable");
  
  // Agrega un evento input para filtrar los resultados cuando se escriba algo
  searchInput.addEventListener("input", function() {
    const filter = searchInput.value.toLowerCase();
    const rows = userTable.getElementsByTagName("tr");

    // Recorre todas las filas de la tabla y oculta las que no coincidan
    for (let i = 0; i < rows.length; i++) {
      const cells = rows[i].getElementsByTagName("td");
      let rowText = "";
      
      // Concatena el texto de todas las celdas de la fila para compararlo con el filtro
      for (let j = 0; j < cells.length; j++) {
        rowText += cells[j].innerText.toLowerCase();
      }

      // Muestra la fila si el texto contiene el filtro, de lo contrario, ocúltala
      if (rowText.indexOf(filter) > -1) {
        rows[i].style.display = "";
      } else {
        rows[i].style.display = "none";
      }
    }
  });
});









//vnetanana modal para borrar y editar usuarios ___________________________________

document.addEventListener("DOMContentLoaded", function() {
  // Llenar el modal de editar con los datos del usuario
  $('#editarModal').on('show.bs.modal', function (event) {
      let button = $(event.relatedTarget);
      let id = button.data('id');
      let nombre = button.data('nombre');
      let apellido = button.data('apellido');
      let email = button.data('email');
      let telefono = button.data('telefono');
      let rol = button.data('rol');

      let modal = $(this);
      modal.find('#editarUsuarioId').val(id);
      modal.find('#editarNombre').val(nombre);
      modal.find('#editarApellido').val(apellido);
      modal.find('#editarEmail').val(email);
      modal.find('#editarTelefono').val(telefono);
      modal.find('#editarRol').val(rol);
      
      // Actualizar la acción del formulario
      $('#editarForm').attr('action', '/editar_usuario/' + id + '/');
  });

  // Llenar el modal de borrar con los datos del usuario
  $('#borrarModal').on('show.bs.modal', function (event) {
      let button = $(event.relatedTarget);
      let id = button.data('id');
      let nombre = button.data('nombre');
      let apellido = button.data('apellido');

      let modal = $(this);
      modal.find('#borrarUsuarioId').val(id);
      modal.find('#borrarNombre').text(nombre);
      modal.find('#borrarApellido').text(apellido);
      
      // Actualizar la acción del formulario
      $('#borrarForm').attr('action', '/borrar_usuario/' + id + '/');
  });
});









//para la ventana modal 
document.addEventListener("DOMContentLoaded", function() {
  const messageElement = document.getElementById('django-messages');
  
  if (messageElement) {
      // Obtener los mensajes desde el div con los mensajes de Django
      const messages = messageElement.getAttribute('data-messages');
      
      if (messages) {
          const messageArray = messages.split(';'); // Convierte el string en un array
          let modalMessage = document.getElementById('modalMessage');
          modalMessage.innerText = messageArray.join(", "); // Combina mensajes si hay múltiples
          
          // Mostrar el modal si hay mensajes
          let resultadoModal = new bootstrap.Modal(document.getElementById('resultadoModal'));
          resultadoModal.show();
      }
  }
});

//

  





(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    if (all) {
      select(el, all).forEach(e => e.addEventListener(type, listener))
    } else {
      select(el, all).addEventListener(type, listener)
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Sidebar toggle
   */
  if (select('.toggle-sidebar-btn')) {
    on('click', '.toggle-sidebar-btn', function(e) {
      select('body').classList.toggle('toggle-sidebar')
    })
  }

  /**
   * Search bar toggle
   */
  if (select('.search-bar-toggle')) {
    on('click', '.search-bar-toggle', function(e) {
      select('.search-bar').classList.toggle('search-bar-show')
    })
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  let selectHeader = select('#header')
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
        selectHeader.classList.add('header-scrolled')
      } else {
        selectHeader.classList.remove('header-scrolled')
      }
    }
    window.addEventListener('load', headerScrolled)
    onscroll(document, headerScrolled)
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Initiate tooltips
   */
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
  })

  /**
   * Initiate quill editors
   */
  if (select('.quill-editor-default')) {
    new Quill('.quill-editor-default', {
      theme: 'snow'
    });
  }

  if (select('.quill-editor-bubble')) {
    new Quill('.quill-editor-bubble', {
      theme: 'bubble'
    });
  }

  if (select('.quill-editor-full')) {
    new Quill(".quill-editor-full", {
      modules: {
        toolbar: [
          [{
            font: []
          }, {
            size: []
          }],
          ["bold", "italic", "underline", "strike"],
          [{
              color: []
            },
            {
              background: []
            }
          ],
          [{
              script: "super"
            },
            {
              script: "sub"
            }
          ],
          [{
              list: "ordered"
            },
            {
              list: "bullet"
            },
            {
              indent: "-1"
            },
            {
              indent: "+1"
            }
          ],
          ["direction", {
            align: []
          }],
          ["link", "image", "video"],
          ["clean"]
        ]
      },
      theme: "snow"
    });
  }

  /**
   * Initiate TinyMCE Editor
   */

  const useDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const isSmallScreen = window.matchMedia('(max-width: 1023.5px)').matches;

  tinymce.init({
    selector: 'textarea.tinymce-editor',
    plugins: 'preview importcss searchreplace autolink autosave save directionality code visualblocks visualchars fullscreen image link media codesample table charmap pagebreak nonbreaking anchor insertdatetime advlist lists wordcount help charmap quickbars emoticons accordion',
    editimage_cors_hosts: ['picsum.photos'],
    menubar: 'file edit view insert format tools table help',
    toolbar: "undo redo | accordion accordionremove | blocks fontfamily fontsize | bold italic underline strikethrough | align numlist bullist | link image | table media | lineheight outdent indent| forecolor backcolor removeformat | charmap emoticons | code fullscreen preview | save print | pagebreak anchor codesample | ltr rtl",
    autosave_ask_before_unload: true,
    autosave_interval: '30s',
    autosave_prefix: '{path}{query}-{id}-',
    autosave_restore_when_empty: false,
    autosave_retention: '2m',
    image_advtab: true,
    link_list: [{
        title: 'My page 1',
        value: 'https://www.tiny.cloud'
      },
      {
        title: 'My page 2',
        value: 'http://www.moxiecode.com'
      }
    ],
    image_list: [{
        title: 'My page 1',
        value: 'https://www.tiny.cloud'
      },
      {
        title: 'My page 2',
        value: 'http://www.moxiecode.com'
      }
    ],
    image_class_list: [{
        title: 'None',
        value: ''
      },
      {
        title: 'Some class',
        value: 'class-name'
      }
    ],
    importcss_append: true,
    file_picker_callback: (callback, value, meta) => {
      /* Provide file and text for the link dialog */
      if (meta.filetype === 'file') {
        callback('https://www.google.com/logos/google.jpg', {
          text: 'My text'
        });
      }

      /* Provide image and alt text for the image dialog */
      if (meta.filetype === 'image') {
        callback('https://www.google.com/logos/google.jpg', {
          alt: 'My alt text'
        });
      }

      /* Provide alternative source and posted for the media dialog */
      if (meta.filetype === 'media') {
        callback('movie.mp4', {
          source2: 'alt.ogg',
          poster: 'https://www.google.com/logos/google.jpg'
        });
      }
    },
    height: 600,
    image_caption: true,
    quickbars_selection_toolbar: 'bold italic | quicklink h2 h3 blockquote quickimage quicktable',
    noneditable_class: 'mceNonEditable',
    toolbar_mode: 'sliding',
    contextmenu: 'link image table',
    skin: useDarkMode ? 'oxide-dark' : 'oxide',
    content_css: useDarkMode ? 'dark' : 'default',
    content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:16px }'
  });

  /**
   * Initiate Bootstrap validation check
   */
  var needsValidation = document.querySelectorAll('.needs-validation')

  Array.prototype.slice.call(needsValidation)
    .forEach(function(form) {
      form.addEventListener('submit', function(event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })

  /**
   * Initiate Datatables
   */
  const datatables = select('.datatable', true)
  datatables.forEach(datatable => {
    new simpleDatatables.DataTable(datatable, {
      perPageSelect: [5, 10, 15, ["All", -1]],
      columns: [{
          select: 2,
          sortSequence: ["desc", "asc"]
        },
        {
          select: 3,
          sortSequence: ["desc"]
        },
        {
          select: 4,
          cellClass: "green",
          headerClass: "red"
        }
      ]
    });
  })

  /**
   * Autoresize echart charts
   */
  const mainContainer = select('#main');
  if (mainContainer) {
    setTimeout(() => {
      new ResizeObserver(function() {
        select('.echart', true).forEach(getEchart => {
          echarts.getInstanceByDom(getEchart).resize();
        })
      }).observe(mainContainer);
    }, 200);
  }

})();

//esta parte es de la tabla asignacion para que el usuario agrege observaciones 
function guardarObservacion(tareaId) {
  const observacion = document.getElementById(`observacion-${tareaId}`).value; // Obtiene el valor de la observación

  console.log('ID de tarea:', tareaId);
  console.log('Observación:', observacion);

  fetch(`/guardar_observacion/${tareaId}/`, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': '{{ csrf_token }}'  // Asegúrate de incluir el token CSRF
      },
      body: JSON.stringify({ observacion: observacion })
  })
  .then(response => {
      return response.json().then(data => {
          if (response.ok) {
              alert('Observación guardada correctamente.');
          } else {
              alert('Error al guardar la observación: ' + data.message);
          }
      });
  })
  .catch(error => {
      console.error('Error:', error);
  });
}

//Mapa que ya quedo---------------------------------------------------------------------------------------------------------------------
// Inicialización del mapa
const map = L.map('map').setView([19.4326, -99.1332], 12); // Centrar el mapa en una ubicación inicial

// Agregar capa de mosaico (tiles)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);


// Función para buscar la dirección ingresada
function buscarDireccion() {
    const direccion = document.getElementById("direccionInput").value.trim();

    // Validar la longitud de la dirección
    if (direccion.length === 0) {
        alert('Por favor, ingrese una dirección.');
        return;
    }
    if (direccion.length > 100) {
        alert('La dirección es demasiado larga. Por favor, ingrese una dirección más corta.');
        return;
    }

    // API de Nominatim para geocodificación
    const url = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(direccion)}&addressdetails=1&limit=1`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.length > 0) {
                const { lat, lon } = data[0]; // Obtener las coordenadas de la primera coincidencia
                map.setView([lat, lon], 15); // Mover el mapa a la ubicación

                // Agregar un marcador en la ubicación
                L.marker([lat, lon]).addTo(map)
                    .bindPopup(`Dirección: ${direccion}`)
                    .openPopup();
            } else {
                alert('No se encontraron resultados para la dirección ingresada. Intente ser más específico.');
            }
        })
        .catch(error => {
            console.error('Error en la búsqueda:', error);
            alert('Error al buscar la dirección. Por favor intenta nuevamente.');
        });
}

// Agregar un evento de escucha al botón de búsqueda
document.getElementById("buscarBtn").addEventListener("click", buscarDireccion);

// Si quieres, también puedes agregar la funcionalidad de búsqueda al presionar Enter
document.getElementById("direccionInput").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        buscarDireccion();
    }
});




//notificacion
const usuarioId = "{{ request.user.id }}";  // Obtén el ID del usuario en el frontend
const socket = new WebSocket(`ws://${window.location.host}/ws/notificaciones/`);

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    alert(data.message);  // Muestra el mensaje como una alerta; puedes personalizar el estilo de la notificación
};

socket.onopen = function() {
    console.log("Conexión WebSocket establecida para notificaciones de tareas.");
};

socket.onclose = function() {
    console.log("Conexión WebSocket cerrada.");
};

// boton de completado
function completarTarea(tareaId) {
  fetch(`/asignar_tarea/completar/${tareaId}/`, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken')  // Asegúrate de obtener el token CSRF
      }
  })
  .then(response => response.json())
  .then(data => {
      if (data.success) {
          alert('Tarea marcada como completada');
          location.reload();  // Recargar la página para actualizar la tabla
      } else {
          alert(data.error || 'Error al completar la tarea');
      }
  })
  .catch(error => console.error('Error:', error));
}

// Función para obtener el token CSRF
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

// aceptar tarea empleado 
function aceptarTarea(tareaId, usuarioId) {
  fetch(`/ruta-a-tu-vista-de-asignar-tarea/${tareaId}`, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken  // Asegúrate de incluir el token CSRF
      },
      body: JSON.stringify({ usuario_id: usuarioId })
  })
  .then(response => response.json())
  .then(data => {
      if (data.success) {
          // Cerrar el modal
          $('#notificacionModal').modal('hide');

          // Añadir la tarea a la tabla si se ha asignado correctamente
          if (data.tarea) {
              const tarea = data.tarea;
              
              // Crear una nueva fila en la tabla
              const nuevaFila = `
                  <tr>
                      <td>${tarea.fecha_asignacion}</td>
                      <td>${tarea.direccion}</td>
                      <td>${tarea.actividad}</td>
                      <td>${tarea.num_cajero}</td>
                  </tr>
              `;
              
              // Insertar la fila en el cuerpo de la tabla
              document.querySelector("table tbody").insertAdjacentHTML("beforeend", nuevaFila);
          }
      } else {
          alert("Hubo un error al aceptar la tarea.");
      }
  })
  .catch(error => {
      console.error("Error:", error);
  });
}

function actualizarActividad(tareaId, nuevaActividad) {
  fetch(`/actualizar_actividad/${tareaId}/`, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken') // Asegúrate de incluir el token CSRF
      },
      body: JSON.stringify({ actividad: nuevaActividad })
  })
  .then(response => response.json())
  .then(data => {
      if (data.success) {
          alert('Actividad actualizada correctamente.');
          location.reload(); // Recargar la página para reflejar los cambios
      } else {
          alert('Error al actualizar la actividad: ' + data.error);
      }
  })
  .catch(error => {
      console.error('Error:', error);
      alert('Hubo un error al actualizar la actividad.');
  });
}

// Función para obtener el token CSRF
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;

}




// SALARIO-----------------------------------------------------------------------------------------------------------------------
// Función para calcular el total automáticamente
// Función para calcular el total automáticamente y validar los campos
function calcularTotal() {
  var viaticos = parseFloat(document.getElementById('viaticos').value) || 0;
  var pagoSitio = parseFloat(document.getElementById('pago_sitio').value) || 0;
  var total = viaticos + pagoSitio;
  
  // Asignar el valor calculado al campo "Total"
  document.getElementById('total').value = total.toFixed(2);
}

function validarFormulario() {
  var viaticos = document.getElementById('viaticos').value;
  var pagoSitio = document.getElementById('pago_sitio').value;

  // Verificar que los valores sean números válidos
  if (isNaN(viaticos) || isNaN(pagoSitio)) {
      alert("Por favor, ingrese valores válidos para Viáticos y Pago Sitio.");
      return false;
  }
  return true;
}

// Asegurarse de que el formulario se valida antes de enviarlo
document.querySelector("form").onsubmit = function(event) {
  if (!validarFormulario()) {
      event.preventDefault();  // Evitar que el formulario se envíe si la validación falla
  }
};

