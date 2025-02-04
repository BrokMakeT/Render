from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Salario, Notificacion, UsuarioCustomizado, Tarea

@receiver(post_save, sender=Salario)
def registrar_notificacion_por_cambio_salario(sender, instance, created, **kwargs):
    # Solo crear una notificación si no es un nuevo registro
    if not created:
        usuario = instance.usuario
        tarea = instance.tarea

        descripcion = (
            f"Se actualizó el salario asociado con la tarea {tarea.id if tarea else 'N/A'} "
            f"y el usuario {usuario.first_name} {usuario.last_name}."
        )

        # Crear la notificación en el modelo Notificacion
        Notificacion.objects.create(
            descripcion=descripcion,
            tarea=tarea,
            usuario=usuario,
        )
