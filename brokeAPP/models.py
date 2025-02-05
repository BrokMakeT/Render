from django.contrib.auth.models import AbstractUser
from django.db import models

# Si necesitas agregar más campos, puedes extender el modelo de usuario de Django
class UsuarioCustomizado(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True, unique=True)
    rol = models.CharField(
        max_length=10,
        choices=[('Admin', 'Admin'), ('Empleado', 'Empleado')],
        default='Empleado'
    )
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'  # Cambia el campo para la autenticación
    REQUIRED_FIELDS = []  # Puedes dejarlo vacío si no tienes campos requeridos adicionales

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Otras tablas como Cliente, Cotizacion, Factura, Tarea, etc.

from django.db import models

class Tarea(models.Model):
    # Campos previamente definidos
    descripcion = models.CharField(max_length=255)
    fecha_anclaje = models.CharField(max_length=20, null=True, blank=True)
    hora_anclaje = models.CharField(max_length=10, null=True, blank=True)
    fecha_vencimiento = models.CharField(max_length=20, null=True, blank=True)
    hora_venconfig = models.CharField(max_length=10, null=True, blank=True)
    direccion = models.CharField(max_length=255, default="Dirección pendiente")
    actividad = models.CharField(max_length=50, choices=[('Anclaje', 'Anclaje'), ('Configuración', 'Configuración'), ('Fibra', 'Fibra')], default='Anclaje')
    usuario = models.ForeignKey('UsuarioCustomizado', on_delete=models.SET_NULL, null=True, blank=True) 
    confirmacion = models.CharField(max_length=50, choices=[('sin_confirmar', 'Sin Confirmar'), ('confirmado', 'Confirmado'), ('rechazado', 'Rechazado')], default='sin_confirmar')
    num_cajero = models.CharField(max_length=50, unique=True, default="Sin número")  
    observaciones = models.TextField(null=True, blank=True)  
    completada = models.BooleanField(default=False)  
    Cod_postal = models.CharField(max_length=255, default="Dirección pendiente")  
    cordenadas = models.CharField(max_length=255, default="cordenadas pendiente")  

    estado = models.CharField(max_length=20, choices=[('iniciado', 'Iniciado'), ('en_proceso', 'En Proceso'), ('Anclaje_completado', 'Anclaje completado'), ('cancelado', 'Cancelado'), ('completado', 'Completado'), ('pendiente_revision', 'Pendiente de Revisión'), ('reprogramado', 'Reprogramado')], default='pendiente')

    def __str__(self):
        return f"Tarea {self.id}: {self.descripcion}"

    @property
    def asignada(self):
        return self.usuario is not None

    def reset_tarea(self):
        """
        Resetea los campos 'completada' a False y 'confirmacion' a 'sin_confirmar'
        cuando el estado es 'cancelado' o 'reprogramado'.
        """
        if self.estado in ['cancelado', 'reprogramado']:
            self.completada = False
            self.confirmacion = 'sin_confirmar'
            self.save()

    def save(self, *args, **kwargs):
        # Guardar el estado original solo si la tarea ya existe (tiene una pk asignada)
        if self.pk:
            original = Tarea.objects.get(pk=self.pk)
            self._original_estado = original.estado
        else:
            self._original_estado = self.estado

        if self.pk is not None:  # Solo si ya existe la tarea
            original = Tarea.objects.get(pk=self.pk)
            if original.estado != self.estado and self.estado in ['Anclaje_completado', 'cancelado', 'completado', 'reprogramado']:
                # Crea un registro en HistorialTarea si el estado ha cambiado a uno relevante
                HistorialTarea.objects.create(
                    tarea=self,
                    estado=self.estado,
                    fecha_asignacion=self.fecha_anclaje,
                    direccion=self.direccion,
                    actividad=self.actividad,
                    num_cajero=self.num_cajero,
                    asignado_a=self.usuario.username if self.usuario else 'Desconocido',
                )
                # Crear o actualizar registro en Salario
                if self.usuario is not None:
                    from .models import Salario  # Importación local para evitar dependencias circulares
                    Salario.objects.get_or_create(
                        usuario=self.usuario,
                        tarea=self
                    )

        super().save(*args, **kwargs)  # Llama al método save original

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Usamos el modelo User si no tienes un modelo de usuario personalizado.
# Si tienes un modelo personalizado de usuario, puedes referenciarlo directamente.
UsuarioCustomizado = get_user_model()

class Notificacion(models.Model):
    descripcion = models.TextField()
    usuario = models.ForeignKey(UsuarioCustomizado, on_delete=models.CASCADE, null=True)  # Permitir nulos
    tarea = models.ForeignKey('Tarea', on_delete=models.CASCADE, null=False)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    leida = models.BooleanField(default=False)


    def __str__(self):
        return f"Notificación {self.id}: {self.descripcion[:50]}..."

class TareaAvanzada(Tarea):
    prioridad = models.CharField(max_length=50, choices=[('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja')], default='Media')
    responsable = models.CharField(max_length=100, null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Tarea Avanzada {self.id}: {self.descripcion} (Prioridad: {self.prioridad})"

# TABLAS.HTML---------------------------------------------------------------------------------------------------------------------
from django.db import models

class HistorialTarea(models.Model):
    tarea = models.ForeignKey('Tarea', on_delete=models.CASCADE, related_name='historial')
    estado = models.CharField(max_length=20)  # Estado de la tarea en el historial
    fecha_asignacion = models.DateTimeField(null=True, blank=True)  # Fecha de asignación (cambia a DateTimeField)
    direccion = models.CharField(max_length=255)  # Dirección
    actividad = models.CharField(max_length=50)  # Actividad
    num_cajero = models.CharField(max_length=50)  # Número de cajero
    asignado_a = models.CharField(max_length=255, null=True, blank=True)  # Usuario asignado
    fecha_registro = models.DateTimeField(auto_now_add=True)  # Fecha y hora de creación del historial

    def __str__(self):
        # Verifica si la descripción está vacía y asigna un valor por defecto
        descripcion = self.tarea.descripcion if self.tarea.descripcion else "Sin descripción"
        return f"Historial - {self.estado} - {descripcion}"



class Salario(models.Model):
    usuario = models.ForeignKey('UsuarioCustomizado', on_delete=models.CASCADE)
    tarea = models.ForeignKey('Tarea', on_delete=models.CASCADE)
    viaticos = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Permite valores nulos
    pago_sitio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Permite valores nulos
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Permite valores nulos

    def __str__(self):
        return f"Salario de {self.usuario} para tarea {self.tarea.id}"

