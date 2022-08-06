from django.contrib import admin
from .models import Employee


# Register your models here.

@admin.register(Employee)
class EmpAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "dept", "age", "create_at"]
