from .models import Notificacion

def crear_notificacion(usuario, tipo, descripcion):
    """
    Crea una notificación para un usuario específico.
    """
    Notificacion.objects.create(
        usuario=usuario,
        tipo=tipo,
        descripcion=descripcion
    )
