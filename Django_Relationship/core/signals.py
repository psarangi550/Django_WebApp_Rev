from django.db.models.signals import post_delete
from core.models import Equipment, WFMTInfo
from django.dispatch import receiver


@receiver(post_delete, sender=WFMTInfo)
def recv_pre_delete(sender, instance, using="default", **kwargs):
    equip_obj = instance.equipment
    equip_obj.delete()


    # equip_obj.delete()
