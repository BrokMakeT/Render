# brokeM/routing.py
from django.urls import path
from tu_app.consumers import NotificacionConsumer  # Cambia 'tu_app' al nombre de tu aplicación

websocket_urlpatterns = [
    path("ws/notificaciones/", NotificacionConsumer.as_asgi()),  # Ruta para las notificaciones en tiempo real
]
