from django.db.models.signals import pre_save
from .models import Book
from django.dispatch import receiver
from django.template.defaultfilters import slugify


@receiver(pre_save, sender=Book)
def recv_pre_save(sender, instance, raw=False, using="default", **kwargs):
    name = instance.name
    instance.slug = slugify(name)
    return instance
