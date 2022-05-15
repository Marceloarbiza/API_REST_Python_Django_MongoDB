from django.apps import AppConfig


class ProviderappConfig(AppConfig):
    """ AppConfig class to map the app name with the app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ProviderApp'
