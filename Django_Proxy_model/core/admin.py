from django.contrib import admin
from .models import Equipments, EquipmentProxy


# Register your models here.
@admin.register(Equipments)
class EqupAdmin(admin.ModelAdmin):
    list_display = ["id", "cp_number", "sne_id", "trs_area"]


@admin.register(EquipmentProxy)
class EqupProxyAdmin(admin.ModelAdmin):
    list_display = ["id", "cp_number", "sne_id", "trs_area"]
