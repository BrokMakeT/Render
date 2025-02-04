# Tu aplicación -> brokeapp1/context_processors.py
from .models import Notificacion

def notificaciones_usuario(request):
    if request.user.is_authenticated:
        notificaciones = Notificacion.objects.filter(usuario=request.user).order_by('-fecha_creacion')
        notificaciones_no_leidas = notificaciones.filter(leida=False)
        return {
            'notificaciones': notificaciones,
            'notificaciones_no_leidas': notificaciones_no_leidas,
        }
    return {}
