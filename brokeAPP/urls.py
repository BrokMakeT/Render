from django.urls import path
from . import views  # Asegúrate de importar views
from django.urls import path
from . import views

from .views import listar_tareas, guardar_observacion, completar_tarea

from .views import listar_tareas
from django.urls import path
from django.urls import path
from .views import cambiar_estado_tarea



urlpatterns = [
    # Aquí defines una ruta para tu vista de perfil recuerda que al tener base de datos en tablas las vistas cambian
    #   # Aquí defines una ruta para tu vista de perfil
    path('dashboardA/', views.dashboardA_view, name='dashboardA'),  # Aquí defines una ruta para tu vista de perfil
    path('loginAdmin/', views.loginAdmin_view, name='loginAdmin'),  # Aquí defines una ruta para tu vista de perfil
    path('loginUser/', views.loginUser_view, name='loginUser'),  # Aquí defines una ruta para tu vista de perfil
    path('Registrar/', views.Registrar_view, name='Registrar'),  # Aquí defines una ruta para tu vista de perfil
    path('Correo/', views.Correo_view, name='Correo'),  # Aquí defines una ruta para tu vista de perfil
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),  # Aquí defines una ruta para tu vista de perfil
    path('empleadosPrueba/', views.empleados, name='empleadosPrueba'),  # Aquí defines una ruta para tu vista de perfil
    
    
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('editar_usuario/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('borrar_usuario/<int:id>/', views.borrar_usuario, name='borrar_usuario'),

    
    
    path('asignar/', listar_tareas, name='asignar'),
    path('asignar_tarea/<int:tarea_id>/', views.asignar_tarea, name='asignar_tarea'),
    


#tareas ya asignadas____________________________

    path('modificar_asignacion/<int:tarea_id>/', views.modificar_asignacion, name='modificar_asignacion'),  # Asegúrate de esta línea

#elogin a usuarios_______________________________

    path('login/', views.login_view, name='login'),
    path('loginE/', views.login_employee_view, name='loginE'),
    
#cerrar sesion_______________________________________

    path('logout/', views.logout_view, name='logout'),


#_____________________discord Gael_________________________

path('AccesoUs/', views.AccesoUs_view, name='AccesoUs'),


path('PagoUsuario/', views.ver_salarios, name='PagoUsuario'),

path('enviar_mensajeD/', views.enviar_mensajeD, name='enviar_mensajeD'),


path('chatAdmin/', views.chatAdmin, name='chatAdmin'),










#_______________________correos__________________________________


# brokeAPP/urls.py




path('enviar_correo/', views.enviar_correo_view, name='enviar_correo'),




#Observaciones tabla asignar 

 path('guardar_observacion/<int:tarea_id>/', guardar_observacion, name='guardar_observacion'),
 path('asignar_tarea/completar/<int:tarea_id>/', views.completar_tarea, name='completar_tarea'),
 path('api/actualizar_estado/', views.actualizar_estado, name='actualizar_estado'),
 path('cargar_excel/', views.cargar_excel, name='cargar_excel'),
#path('guardar_observacion/<int:tarea_id>/', guardar_observacion, name='guardar_observacion'),




    
    path('actualizar_actividad/<int:tarea_id>/', views.actualizar_actividad, name='actualizar_actividad'),
    path('actualizar_tarea/', views.actualizar_tarea, name='actualizar_tarea'),
    path('generar-reporte-excel/', views.generar_reporte_excel, name='generar_reporte_excel'),
    path('borrar-datos-y-generar-excel/', views.borrar_datos_y_generar_excel, name='borrar_datos_y_generar_excel'),
    path('actualizar-descripcion/', views.actualizar_descripcion, name='actualizar_descripcion'),




    path('tarea/<int:tarea_id>/cambiar_estado/', cambiar_estado_tarea, name='cambiar_estado_tarea'),


    path('tablas/', views.tablas, name='tablas'),



    path('api/tarea/<int:id>/', views.obtener_tarea, name='obtener_tarea'),




    
    
    path('tareas/empleado/', views.tareas_empleado, name='tareas_empleado'),

    path('confirmar_actividad/<int:tarea_id>/', views.confirmar_actividad, name='confirmar_actividad'),


    path('reagendar_tarea/<int:tarea_id>/', views.reagendar_tarea, name='reagendar_tarea'),

    
]
