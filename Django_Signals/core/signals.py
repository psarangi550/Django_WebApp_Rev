from django.db.models.signals import pre_save, post_save, pre_delete, post_delete, pre_init, post_init
from django.core.signals import request_started, request_finished, got_request_exception
from django.core.handlers.wsgi import WSGIHandler
from django.db.models.signals import pre_migrate
from core.models import Book
from core.apps import CoreConfig
from django.apps import AppConfig
from django.dispatch import receiver  # importing the recevier decorator


@receiver(signal=pre_init, sender=Book)
def recv_pre_init(sender, *args, **kwargs):
    print("Running pre the signal")
    print(sender)
    print(args)
    print(kwargs)


@receiver(signal=post_init, sender=Book)
def recv_post_init(sender, instance, **kwargs):
    print("Running post the signal")
    print(sender)
    print(instance)
    print(kwargs)


@receiver(signal=pre_save, sender=Book)
def recv_pre_save(sender, instance, raw=True, using='default', **kwargs):
    print("Saving the signal")
    print(sender)
    print(instance)
    print(raw)
    print(kwargs)


@receiver(signal=post_save, sender=Book)
def recv_post_save(sender, instance, created, raw=True, using='default', **kwargs):
    print("Saving the signal")
    print(sender)
    print(instance)
    print(created)
    print(raw)
    print(kwargs)


def recv_pre_delete(sender, instance, using='default', **kwargs):
    print("delete the signal")
    print(sender)
    print(instance)
    print(using)
    print(kwargs)


pre_delete.connect(recv_pre_delete, sender=Book)


def recv_post_delete(sender, instance, using="default", **kwargs):
    print(sender)
    print(instance)
    print(kwargs)


post_delete.connect(recv_post_delete, sender=Book)


@receiver(signal=request_started, sender=WSGIHandler)
def recv_request_init(sender, environ, **kwargs):
    print(sender)
    print(environ)
    print(kwargs)


@receiver(signal=request_finished, sender=WSGIHandler)
def recv_request_post(sender, **kwargs):
    print(sender)
    print(kwargs)


def recv_exp(sender, request, **kwargs):
    print(sender)
    print(request)
    print(kwargs)


got_request_exception.connect(recv_exp, sender=None)


