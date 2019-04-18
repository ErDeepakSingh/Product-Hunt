from django.apps import AppConfig
from . import signals

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        from . import signals