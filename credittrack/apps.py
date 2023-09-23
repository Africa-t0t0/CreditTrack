from django.apps import AppConfig

class CredittrackConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'credittrack'

    def ready(self):
        import credittrack.signals