from django.apps import AppConfig
from django.db.models.signals import pre_migrate, post_migrate


def recv_pre_migrate(sender, **kwargs):
    print(sender)
    print(kwargs)


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        post_migrate.connect(recv_pre_migrate, sender=self)
