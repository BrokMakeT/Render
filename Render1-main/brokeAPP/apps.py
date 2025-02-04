from django.apps import AppConfig


class BrokeappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'brokeAPP'


    
from django.apps import AppConfig

class BrokeappConfig(AppConfig):
    name = 'brokeAPP'

    def ready(self):
        import brokeAPP.signals  # Asegúrate de importar las señales
