

from io import BytesIO
from io import BytesIO
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Tarea


from django.utils.decorators import method_decorator

from .models import Tarea  # Asegúrate de importar tu modelo
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404


from django.shortcuts import render, redirect

from django.contrib import messages



from .models import Tarea
from .forms import TareaForm
from .models import Tarea
from .models import UsuarioCustomizado 

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


#para corroborar los usuarios______________________________________inicio
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


#para corroborar los usuarios______________________________________end

from .decorators import admin_required



from django.contrib.auth import login  # Importa la función login de Django


from django.contrib.auth import login as auth_login  # Renombrar la función de inicio de sesión de Django
from django.contrib.auth import get_user_model
Usuario = get_user_model()  # Obtiene el modelo de usuario actual

from django.contrib.auth import authenticate, login

import re

from django.db import IntegrityError

from django.contrib.auth import update_session_auth_hash


from django.contrib.auth import logout  


#discord_____________________________
import asyncio
import discord
from django.http import HttpResponse
from django.conf import settings


#correos_______________________________
from django.core.mail import EmailMessage
from django.conf import settings

from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import enviar_correo_mailjet

def index(request):
    return render(request, 'brokeAPP/index.html')

@admin_required
def asignar_view(request):
    return render(request, 'brokeapp1/asignar.html')  # Cambia 'brokeapp1/profile.html' según tu estructura de carpetas
# Cambia 'brokeapp1/profile.html' según tu estructura de carpetas

@admin_required
# Cambiadef dashboardA_view(request):
# Cambia return render(request, 'brokeapp1/dashboardA.html')  # Cambia 'brokeapp1/profile.html' según tu estructura de carpetas

#error con csrf error 

def csrf_failure(request, reason=""):
    return render(request, 'brokeapp1/csrf_failure.html', status=403)


def loginAdmin_view(request):
    return render(request, 'brokeapp1/loginAdmin.html')  # Cambia 'brokeapp1/profile.html' según tu estructura de carpetas
    
def loginUser_view(request):
    return render(request, 'brokeapp1/loginUser.html')  # Cambia 'brokeapp1/profile.html' según tu estructura de carpetas
@admin_required
def Registrar_view(request):
    return render(request, 'brokeapp1/Registrar.html')  # Cambia 'brokeapp1/profile.html' según tu estructura de carpetas
@admin_required
def Correo_view(request):
    return render(request, 'brokeapp1/Correo.html')  # Cambia 'brokeapp1/profile.html' según tu estructura de carpetas

def empleados(request):
    return render(request, 'brokeapp1/components-buttons.html')  # Cambia 'brokeapp1/profile.html' según tu estructura de carpetas

@admin_required
def chatAdmin(request):
    return render(request, 'brokeapp1/chatAdmin.html')  # Cambia 'brokeapp1/profile.html' según tu estructura de carpetas


# registro de usuarios 


def crear_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono', '')
        rol = request.POST.get('rol', 'Empleado')
        contrasena = request.POST.get('contrasena')
        confirmar_contrasena = request.POST.get('confirmar_contrasena')

        # Validar que las contraseñas coincidan
        if contrasena != confirmar_contrasena:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'brokeapp1/Registrar.html')

        # Validar que el nombre y apellido solo contengan letras
        if not re.match("^[A-Za-záéíóúÁÉÍÓÚÑñ ]+$", nombre):
            messages.error(request, 'El nombre solo puede contener letras.')
            return render(request, 'brokeapp1/Registrar.html')

        if not re.match("^[A-Za-záéíóúÁÉÍÓÚÑñ ]+$", apellido):
            messages.error(request, 'El apellido solo puede contener letras.')
            return render(request, 'brokeapp1/Registrar.html')

        # Genera un username a partir del nombre y apellido
        username = f"{nombre}.{apellido}".lower()

        # Crea una instancia del usuario personalizado
        usuario = UsuarioCustomizado(
            username=username,
            first_name=nombre,
            last_name=apellido,
            email=email,
            telefono=telefono,
            rol=rol
        )

        # Guarda el usuario en la base de datos
        try:
            usuario.set_password(contrasena)  # Establece la contraseña de manera segura
            usuario.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('lista_usuarios')  # Redirige a la vista correspondiente
        except IntegrityError:
            messages.error(request, 'El número de teléfono ya está en uso. Por favor, ingrese uno diferente.')
        except Exception as e:
            messages.error(request, f'Error al registrar usuario: {str(e)}')

    return render(request, 'brokeapp1/Registrar.html')

#editar y borrar_____________________________________________________________

def lista_usuarios(request):
    usuarios = Usuario.objects.all()  # Obtén todos los usuarios
    return render(request, 'brokeapp1/lista_usuarios.html', {'usuarios': usuarios})


def editar_usuario(request, id):
    usuario = UsuarioCustomizado.objects.get(id=id)
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        rol = request.POST.get('rol')
        password = request.POST.get('password')
        confirmar_password = request.POST.get('confirmar_password')

        # Actualiza los campos básicos
        usuario.first_name = nombre
        usuario.last_name = apellido
        usuario.email = email
        usuario.telefono = telefono
        usuario.rol = rol
        
        # Si se ha proporcionado una nueva contraseña
        if password:
            if password == confirmar_password:
                usuario.set_password(password)  # Establece la nueva contraseña
                update_session_auth_hash(request, usuario)  # Actualiza la sesión para que no se cierre al cambiar la contraseña
                messages.success(request, 'Contraseña actualizada correctamente.')
            else:
                messages.error(request, 'Las contraseñas no coinciden.')
                return render(request, 'brokeapp1/editar_usuario.html', {'usuario': usuario})

        try:
            usuario.save()  # Guarda los cambios en el usuario
            messages.success(request, 'Usuario actualizado correctamente.')
            return redirect('lista_usuarios')  # Cambia esta redirección según sea necesario
        except Exception as e:
            messages.error(request, f'Error al actualizar usuario: {str(e)}')
    
    return render(request, 'brokeapp1/editar_usuario.html', {'usuario': usuario})

def borrar_usuario(request, id):
    UsuarioCustomizado = get_user_model()
    usuario = get_object_or_404(UsuarioCustomizado, id=id)
    try:
        usuario.delete()
        messages.success(request, 'Usuario borrado correctamente.')
    except Exception as e:
        messages.error(request, f'Error al borrar usuario: {str(e)}')
    return redirect('lista_usuarios')



# asignar tareas-----------------------------------------------------




# Vista para listar las tareas
@admin_required
def listar_tareas(request):
    tareas_no_asignadas = Tarea.objects.filter(usuario__isnull=True)  # Tareas no asignadas
    tareas_asignadas = Tarea.objects.filter(usuario__isnull=False, completada=False)  # Tareas asignadas pero no completadas
    tareas_completadas = Tarea.objects.filter(completada=True)  # Tareas completadas
    usuarios = Usuario.objects.all()  # Obtener todos los usuarios

    return render(request, 'brokeapp1/asignar.html', {
        'tareas_no_asignadas': tareas_no_asignadas,
        'tareas_asignadas': tareas_asignadas,
        'tareas_completadas': tareas_completadas,
        'usuarios': usuarios
    })


@csrf_exempt
def asignar_tarea(request, tarea_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        usuario_id = data.get('usuario_id')

        if not usuario_id:
            return JsonResponse({'success': False, 'error': 'No se ha proporcionado un usuario'})

        try:
            tarea = Tarea.objects.get(id=tarea_id)
            usuario = UsuarioCustomizado.objects.get(id=usuario_id)  # Cambia aquí para usar UsuarioCustomizado
            tarea.usuario = usuario  # Asignar el usuario a la tarea
            tarea.save()  # Guardar los cambios

            return JsonResponse({'success': True})
        except Tarea.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Tarea no encontrada'})
        except UsuarioCustomizado.DoesNotExist:  # Cambia aquí para usar UsuarioCustomizado
            return JsonResponse({'success': False, 'error': 'Usuario no encontrado'})

    return JsonResponse({'success': False, 'error': 'Método no permitido'})
#tareas ya asignadas________________________________________________________
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Tarea, UsuarioCustomizado

@csrf_exempt
def completar_tarea(request, tarea_id):
    if request.method == 'POST':
        print("Solicitud para completar tarea recibida")  # Mensaje de depuración
        try:
            tarea = Tarea.objects.get(id=tarea_id)
            tarea.completada = True
            tarea.save()
            return JsonResponse({'success': True})
        except Tarea.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Tarea no encontrada'})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})





def modificar_asignacion(request, tarea_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Cargar el cuerpo de la solicitud JSON
            usuario_id = data.get('usuario_id')
            tarea = get_object_or_404(Tarea, id=tarea_id)

            # Obtener el usuario asociado
            usuario = get_object_or_404(Usuario, id=usuario_id)

            # Asignar el nuevo usuario a la tarea
            tarea.usuario = usuario

            # Cambiar el atributo 'confirmacion' a dato de 'sin_confirmar'
            tarea.confirmacion = "sin_confirmar"
            tarea.save()

            return JsonResponse({'message': 'Asignación modificada exitosamente.'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

#para error con csrf_______________________________________
from django.shortcuts import render

def csrf_failure(request, reason=""):
    return render(request, 'brokeapp1/csrf_failure.html', status=403)

#para verificar usuarios Administrador_______________________________________
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Autenticar al usuario con su email
        usuario = authenticate(request, username=email, password=password)

        if usuario is not None:
            login(request, usuario)  # Inicia sesión usando el sistema de autenticación de Django
            if usuario.rol == 'Admin':
                return redirect('dashboardA')  # Redirige al panel de administrador
            else:
                messages.error(request, 'Credenciales inválidas.')  # Redirige al panel de empleados
                
        else:
            messages.error(request, 'Credenciales inválidas comprueba tu usuario.')
    
    return render(request, 'brokeapp1/index.html')  # Renderiza la página de login


#para verificar usuarios Empleado_______________________________________

@csrf_exempt
def login_employee_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Autenticar al usuario
        usuario = authenticate(request, username=email, password=password)

        if usuario is not None:
            login(request, usuario)  # Inicia sesión usando el sistema de autenticación de Django
            if usuario.rol == 'Empleado':
                return redirect('AccesoUs')  # Redirige al panel de empleados
            else:
                messages.error(request, 'No tienes acceso a la parte de empleados.')
                return redirect('home')  # Redirige al login de administradores
        else:
            messages.error(request, 'Credenciales inválidas comprueba tu usuario.')

    return render(request, 'brokeapp1/index.html')  # Renderiza la página de login




#cerrar sesion_________________________________________________________________________________________________________

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('home')  # Redirige al login

#discord _________________________________________________________________________________________________________

def Ubica_view(request):
    return render(request, 'brokeapp1/ubica.html')

def AccesoUs_view(request):
    return render(request, 'brokeapp1/AccesoUs.html')

def PagoUsuario_view(request):
    return render(request, 'brokeapp1/PagoUsuario.html')


 
async def enviar_mensaje_a_discord(mensaje):
    client = discord.Client(intents=discord.Intents.default())
    await client.login(TOKEN)
    channel = await client.fetch_channel(CHANNEL_ID)
    await channel.send(mensaje)
    await client.close()
 
def enviar_mensajeD(request):
    if request.method == 'POST':
        # Obtén el mensaje personalizado del formulario o request POST
        mensaje_personalizado = request.POST.get('mensaje', 'Hola desde Django!')
        # Envía el mensaje usando discord.py
        asyncio.run(enviar_mensaje_a_discord(mensaje_personalizado))
        return HttpResponse("Mensaje enviado a Discord!")
    else:
        return HttpResponse("Método no soportado.", status=405)



import base64

from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import enviar_correo_mailjet

def enviar_correo_view(request):
    if request.method == 'POST':
        destinatario = request.POST['destinatario']
        asunto = request.POST['asunto']
        mensaje = request.POST['mensaje']
        archivo_adjunto = request.FILES.get('archivo')
        
        adjunto_b64 = None
        archivo_nombre = None
        if archivo_adjunto:
            adjunto_b64 = base64.b64encode(archivo_adjunto.read()).decode('utf-8')
            archivo_nombre = archivo_adjunto.name

        if enviar_correo_mailjet(destinatario, asunto, mensaje, adjunto_b64, archivo_nombre):
            messages.success(request, 'Correo enviado con éxito.')
        else:
            messages.error(request, 'Hubo un error al enviar el correo.')
        
        return redirect('enviar_correo')
    
    return render(request, 'brokeapp1/correo.html')




#Funcion de observaciones Tabla asignar
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
import json
from .models import Tarea

@csrf_exempt  # Si estás manejando el CSRF manualmente, pero es mejor usar el token CSRF
@require_POST
def guardar_observacion(request, tarea_id):
    data = json.loads(request.body)
    observacion = data.get('observacion')

    try:
        tarea = Tarea.objects.get(id=tarea_id)
        tarea.observaciones = observacion
        tarea.save()
        return JsonResponse({'message': 'Observación guardada.'}, status=200)
    except Tarea.DoesNotExist:
        return JsonResponse({'message': 'Tarea no encontrada.'}, status=404)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=500)

def vista_ubica(request):
    tareas = Tarea.objects.values('fecha_asignacion', 'direccion', 'actividad', 'num_cajero')
    return render(request, 'ubica.html', {'tareas': tareas})


# Estado de la tabla proceso 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Tarea
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TareaAvanzada  # Asegúrate de importar la clase correcta
import json

@csrf_exempt
def actualizar_estado(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            tarea_id = data.get("id")
            nuevo_estado = data.get("estado")

            # Verificar que el estado proporcionado sea válido
            ESTADOS_VALIDOS = ['iniciado', 'en_proceso','Anclaje_completado', 'cancelado', 'completado', 'pendiente_revision', 'reprogramado']
            if nuevo_estado not in ESTADOS_VALIDOS:
                return JsonResponse({"success": False, "error": "Estado inválido. Los estados permitidos son: " + ", ".join(ESTADOS_VALIDOS)})

            # Buscar la tarea y actualizar su estado
            tarea = Tarea.objects.get(id=tarea_id)
            tarea.estado = nuevo_estado
            tarea.save()

            return JsonResponse({"success": True, "message": f"Estado actualizado exitosamente a {nuevo_estado}"})
        except Tarea.DoesNotExist:
            return JsonResponse({"success": False, "error": "Tarea no encontrada"})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    else:
        return JsonResponse({"success": False, "error": "Método no permitido"})


import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarea

from django.shortcuts import render
from django.http import JsonResponse


from django.shortcuts import render, redirect
from django.contrib import messages


from django.core.exceptions import ValidationError  # Importar ValidationError


def cargar_excel(request):
    if request.method == "POST" and request.FILES.get("archivo_excel"):
        archivo_excel = request.FILES["archivo_excel"]
        try:
            # Leer el archivo Excel
            df = pd.read_excel(archivo_excel)

            # Verificar si las columnas 'LATITUD' y 'LONGITUD' existen
            if 'LATITUD' not in df.columns or 'LONGITUD' not in df.columns:
                raise ValidationError("Faltan las siguientes columnas requeridas: LATITUD o LONGITUD")
            
            # Procesar cada fila del archivo y cargarla en la base de datos
            for index, row in df.iterrows():
                direccion = row['direccion']
                Cod_postal = row['Cod_postal'] if 'Cod_postal' in row else None
                num_cajero = row['num_cajero']
                fecha_anclaje = row['ENTREGA/ANCLAJE']
                hora_anclaje = row['HORA DE ENTREGA']
                fecha_vencimiento = row['CONFIG']
                hora_venconfig = row['HORA LOCAL']
                
                # Combinar LATITUD y LONGITUD en el formato 'LATITUD,LONGITUD'
                latitud = str(row['LATITUD'])
                longitud = str(row['LONGITUD'])
                cordenadas = f"{latitud},{longitud}"

                # Crear la tarea
                Tarea.objects.create(
                    direccion=direccion,
                    Cod_postal=Cod_postal,
                    num_cajero=num_cajero,
                    fecha_anclaje=fecha_anclaje,
                    hora_anclaje=hora_anclaje,
                    fecha_vencimiento=fecha_vencimiento,
                    hora_venconfig=hora_venconfig,
                    cordenadas=cordenadas,  # Almacenar las cordenadas
                )

            # Agregar un mensaje de éxito
            messages.success(request, "Archivo procesado correctamente.")
            return redirect('asignar')  # Redirige a la página principal de asignar tareas
        
        except ValidationError as e:
            # Agregar un mensaje de error
            messages.error(request, f"Error de validación: {str(e)}")
        except Exception as e:
            # Agregar un mensaje de error
            messages.error(request, f"Error al procesar el archivo: {str(e)}")
        
        return redirect('asignar')  # Redirige incluso si hubo errores
    else:
        # Agregar un mensaje para métodos no permitidos
        messages.error(request, "Método no permitido.")
        return redirect('asignar')





# ______________________________________________________para guardar la descripcion:______________________________


from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Tarea

def actualizar_descripcion(request):
    if request.method == "POST":
        # Obtener el id de la tarea y la nueva descripción del formulario
        tarea_id = request.POST.get('tarea_id')
        nueva_descripcion = request.POST.get('descripcion')

        # Obtener la tarea correspondiente
        tarea = get_object_or_404(Tarea, id=tarea_id)

        # Actualizar la descripción
        tarea.descripcion = nueva_descripcion
        tarea.save()

        # Retornar una respuesta en JSON para confirmar la actualización
        return JsonResponse({'mensaje': 'Descripción actualizada exitosamente.'})

    return redirect('asignar')  # Si no es POST, redirigir a la vista principal












@csrf_exempt
def actualizar_actividad(request, tarea_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nueva_actividad = data.get('actividad')

            if not nueva_actividad:
                return JsonResponse({'success': False, 'error': 'No se proporcionó una actividad'})

            tarea = Tarea.objects.get(id=tarea_id)
            tarea.actividad = nueva_actividad

            # Resetear usuario solo si la actividad cambia a "Configuración"
            if nueva_actividad == "Configuración":
                tarea.usuario = None  # Reinicia el usuario asignado
                tarea.estado = "Pendiente"  # Opcional: Reinicia el estado
                tarea.completada = 0
                tarea.confirmacion = "sin_confirmar"
            tarea.save()

            return JsonResponse({'success': True, 'message': 'Actividad actualizada exitosamente'})
        except Tarea.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Tarea no encontrada'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'success': False, 'error': 'Método no permitido'})





def vista_tareas(request):
    tareas_completadas = Tarea.objects.filter(estado="Anclaje_completado")  # Tareas en la tabla de Anclajes Completados
    tareas_no_asignadas = Tarea.objects.filter(actividad="Configuración", estado="Pendiente")  # Tareas para Configuraciones
    usuarios = Usuario.objects.all()  # Usuarios disponibles para asignar

    return render(request, 'nombre_template.html', {
        'tareas_completadas': tareas_completadas,
        'tareas_no_asignadas': tareas_no_asignadas,
        'usuarios': usuarios,
    })

#para boton de finalizar tarea
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def actualizar_tarea(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            tarea_id = data.get("id")
            nuevo_estado = data.get("estado")

            # Buscar la tarea por ID
            tarea = Tarea.objects.get(id=tarea_id)
            
            # Si la tarea está en estado "en_proceso", cambiarla a "finalizado"
            if nuevo_estado == 'finalizado':
                tarea.estado = 'finalizado'
                tarea.completada = 1  # Marcar la tarea como completada
                tarea.save()

            return JsonResponse({"success": True, "message": "Estado actualizado exitosamente"})
        except Tarea.DoesNotExist:
            return JsonResponse({"success": False, "error": "Tarea no encontrada"})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    else:
        return JsonResponse({"success": False, "error": "Método no permitido"})


        #para generar reportes de las tareas____________________________________________
import openpyxl
from django.http import HttpResponse
from .models import Tarea

def generar_reporte_excel(request):
    # Crear un libro de trabajo de Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Tareas"

    # Escribir los encabezados de las columnas
    headers = [
        "ID", "Descripción", "Fecha Vencimiento", "Dirección", "Actividad", 
        "Usuario", "Num Cajero", "Observaciones", "Completada", "Cod Postal", 
        "Estado", "Fecha Anclaje", "Hora Anclaje", "Hora Ven Config", "Cordenadas"
    ]
    ws.append(headers)

    # Obtener las tareas
    tareas = Tarea.objects.all()

    # Escribir los datos de cada tarea en el archivo Excel
    for tarea in tareas:
        descripcion = tarea.descripcion or "No disponible"
        fecha_vencimiento = str(tarea.fecha_vencimiento) if tarea.fecha_vencimiento else "No disponible"
        direccion = tarea.direccion or "No disponible"
        actividad = tarea.actividad or "No disponible"
        usuario = f"{tarea.usuario.first_name} {tarea.usuario.last_name}" if tarea.usuario else "No asignado"
        num_cajero = tarea.num_cajero or "No disponible"
        observaciones = tarea.observaciones or "No disponible"
        completada = str(tarea.completada) if tarea.completada is not None else "No disponible"
        estado = tarea.estado or "No disponible"
        fecha_anclaje = str(tarea.fecha_anclaje) if tarea.fecha_anclaje else "No disponible"
        hora_anclaje = str(tarea.hora_anclaje) if tarea.hora_anclaje else "No disponible"
        hora_venconfig = str(tarea.hora_venconfig) if tarea.hora_venconfig else "No disponible"
        cordenadas = tarea.cordenadas or "No disponible"

        # Comprobamos si el campo Cod_postal existe en el modelo
        cod_postal = getattr(tarea, 'Cod_postal', None) or "No disponible"

        # Escribir una fila con los datos de la tarea
        ws.append([
            tarea.id, descripcion, fecha_vencimiento, direccion, actividad, 
            usuario, num_cajero, observaciones, completada, cod_postal, 
            estado, fecha_anclaje, hora_anclaje, hora_venconfig, cordenadas
        ])

    # Crear la respuesta HTTP con el archivo Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="reporte_tareas.xlsx"'

    # Guardar el archivo Excel en la respuesta
    wb.save(response)

    return response




#_______________________________________borrado de tareas___________________________________
from django.db import connection
from django.shortcuts import render, redirect
from django.http import HttpResponse
from openpyxl import Workbook
from .models import Tarea

def borrar_datos_y_generar_excel(request):
    if request.method == 'POST':
        # Generar el archivo Excel antes de borrar los datos
        tareas = Tarea.objects.all()

       
        # Crear el archivo Excel
        wb = Workbook()
        ws = wb.active
        ws.append(["ID", "Descripción", "Fecha de Vencimiento", "Dirección", "Actividad", "Nombre del Usuario", "Num_Cajero", "Observaciones", "Completada", "Cod_postal", "Estado", "Fecha de Anclaje", "Hora de Anclaje", "Hora Venconfig", "Coordenadas"])

        for tarea in tareas:
                ws.append([
                    tarea.id,
                tarea.descripcion,
                tarea.fecha_vencimiento,
                tarea.direccion,
                tarea.actividad,
                f"{tarea.usuario.first_name} {tarea.usuario.last_name}" if tarea.usuario else "No asignado",  # Comprobación añadida
                tarea.num_cajero,
                tarea.observaciones,
                tarea.completada,
                tarea.Cod_postal if tarea.Cod_postal else "No disponible",
                tarea.estado,
                tarea.fecha_anclaje,
                tarea.hora_anclaje,
                tarea.hora_venconfig,
                tarea.cordenadas,
        ])

        # Guardar el archivo Excel
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="tareas_reporte.xlsx"'
        wb.save(response)
        
        # Borrar los datos de la tabla de tareas
        Tarea.objects.all().delete()

        # Reiniciar el contador AUTO_INCREMENT
        with connection.cursor() as cursor:
            cursor.execute("ALTER TABLE brokeapp_tarea AUTO_INCREMENT = 1;")

        # Redirigir después de completar la acción
        return response  # Devuelve el Excel directamente como respuesta
    # Si no es un POST, mostrar un mensaje en la misma página
    return render(request, 'brokeapp1/asignar.html', {
        'mensaje': '¿Está seguro de que desea borrar todas las tareas? Esta acción no se puede deshacer.',
    })

from django.shortcuts import get_object_or_404, redirect
from .models import Tarea, HistorialTarea
 
def cambiar_estado_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    nuevo_estado = request.POST.get('estado')
 
    # Verifica que el estado sea válido
    estados_validos = ['Anclaje_completado', 'cancelado', 'completado']
    if nuevo_estado in estados_validos:
        # Guarda un registro en HistorialTarea
        HistorialTarea.objects.create(
            tarea=tarea,
            estado=nuevo_estado,
            fecha_asignacion=tarea.fecha_anclaje,
            direccion=tarea.direccion,
            actividad=tarea.actividad,
            num_cajero=tarea.num_cajero,
            asignado_a=tarea.usuario
        )
        # Actualiza el estado de la tarea
        tarea.estado = nuevo_estado
        tarea.save()
 
    return redirect('vista_de_tareas')  #
 



# HTML TABLAS-----------------------------------------------------------------------------------------------------------------------
from django.shortcuts import render, redirect
from .models import HistorialTarea, Salario, UsuarioCustomizado
from .forms import SalarioForm

def tablas(request):
    # Obtener los registros de historial de tareas
    sabrina = HistorialTarea.objects.all()

    # Obtener todos los usuarios
    usuarios = UsuarioCustomizado.objects.all()

    # Filtrar salarios por el usuario seleccionado, si se ha elegido uno
    if 'usuario' in request.GET:
        usuario_id = request.GET['usuario']
        salarios = Salario.objects.filter(usuario_id=usuario_id)
    else:
        salarios = Salario.objects.all()  # Si no se selecciona usuario, mostrar todos

    # Verificar si se seleccionó un salario para actualizar
    salario_id = request.GET.get('salario_id')
    salario = None
    if salario_id:
        try:
            salario = Salario.objects.get(id=salario_id)
        except Salario.DoesNotExist:
            salario = None

    # Manejar el formulario de actualización
    if request.method == 'POST':
        salario_id = request.POST.get('salario_id')
        try:
            salario = Salario.objects.get(id=salario_id)
            salario.viaticos = request.POST.get('viaticos')
            salario.pago_sitio = request.POST.get('pago_sitio')
            salario.total = request.POST.get('total')
            salario.save()  # Actualizar el registro
            return redirect('tablas')  # Redirigir a la misma página
        except Salario.DoesNotExist:
            pass

    # Pasar los contextos a la plantilla
    return render(request, 'brokeapp1/tablas.html', {
        'sabrina': sabrina,
        'salarios': salarios,
        'usuarios': usuarios,
        'salario': salario,  # Incluir el salario seleccionado para editar
    })



# HTML DASHBOARD-------------------------------------------------------------------------------------------------------------------

from django.db.models import Count
from django.shortcuts import render
from .models import Tarea, UsuarioCustomizado
import json

def dashboardA_view(request):
    # Contar cuántos usuarios tienen el rol de "Empleado"
    total_empleados = UsuarioCustomizado.objects.filter(rol='Empleado').count()

    # Obtener los administradores con sus nombres
    administradores = UsuarioCustomizado.objects.filter(rol='Admin').values('first_name', 'last_name')

    # Obtener el usuario con más tareas asignadas
    usuario_con_mas_tareas = UsuarioCustomizado.objects.annotate(num_tareas=Count('tarea')).order_by('-num_tareas').first()

    # Obtener el conteo de tareas por estado
    tarea_estados = {
        'Anclaje_completado': Tarea.objects.filter(estado='Anclaje_completado').count(),
        'Reprogramado': Tarea.objects.filter(estado='reprogramado').count(),
        'Completado': Tarea.objects.filter(estado='completado').count(),
        'Cancelado': Tarea.objects.filter(estado='cancelado').count(),
        'Iniciado': Tarea.objects.filter(estado='iniciado').count(),
        'En_Proceso': Tarea.objects.filter(estado='en_proceso').count(),
    }

    # Convertir los datos a formato JSON para usarlos en el script
    tarea_estados_json = json.dumps(tarea_estados)

    # Pasar el contexto a la plantilla
    return render(request, 'brokeapp1/dashboardA.html', {
        'total_empleados': total_empleados,
        'usuario_con_mas_tareas': usuario_con_mas_tareas,
        'tarea_estados_json': tarea_estados_json,
        'administradores': administradores
    })

from django.http import JsonResponse
from .models import Tarea

def obtener_tarea(request, id):
    try:
        tarea = Tarea.objects.get(pk=id)
        data = {
            "id": tarea.id,
            "estado": tarea.estado,
            "actividad": tarea.actividad,
            
        }
        return JsonResponse(data)
    except Tarea.DoesNotExist:
        return JsonResponse({"error": "La tarea no existe."}, status=404)


#VISTA PARA NOTIFICACIONES ____________________________________________________





#vista para que cada usuario pueda ver sus propias tareas___________________
def tareas_empleado(request):
    usuario = request.user  # Usuario autenticado
    tareas = Tarea.objects.filter(usuario=usuario).order_by('-fecha_anclaje')  # Filtrar tareas por usuario y ordenar
    context = {
        'tareas': tareas
    }
    return render(request, 'brokeapp1/ubica.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Tarea

def confirmar_actividad(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)

    if request.method == 'POST':
        accion = request.POST.get('accion')

        if accion == 'aceptar':
            tarea.confirmacion = 'confirmado'
            messages.success(request, f"La actividad {tarea.descripcion} ha sido aceptada.")
        elif accion == 'rechazar':
            tarea.confirmacion = 'rechazado'
            messages.error(request, f"La actividad {tarea.descripcion} ha sido rechazada.")
        
        tarea.save()  # Guardar los cambios en el modelo
        return redirect('tareas_empleado')  # Redirigir a la lista de tareas
    return redirect('tareas_empleado')  # Si no es un POST, redirigir a la lista de tareas



#para ver al usuario de el pago_____________________
from django.shortcuts import render
from .models import Salario

def ver_salarios(request):
    # Obtén el usuario autenticado
    usuario = request.user

    # Filtra los registros de salario para mostrar solo los del usuario autenticado
    salarios = Salario.objects.filter(usuario=usuario)

    # Pasa los salarios al contexto para mostrarlos en la plantilla
    context = {
        'salarios': salarios,
    }
    
    return render(request, 'brokeapp1/PagoUsuario.html', context)

#para reagendar la tarea 

from django.shortcuts import get_object_or_404, redirect
from .models import Tarea

def reagendar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.reset_tarea()  # Llama al método que resetea los campos
    return redirect('asignar')  # Redirige a la vista que desees




