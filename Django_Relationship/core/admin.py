from django.contrib import admin
from .models import Equipment, PACSData


# Register your models here.
@admin.register(Equipment)
class EquipAdmin(admin.ModelAdmin):
    list_display = ["id", "cp_number", "sne_id", "trs_area"]


@admin.register(PACSData)
class PACSDataAdmin(admin.ModelAdmin):
    list_display = ["id", "equipment", "scheme_number", "model_type"]
