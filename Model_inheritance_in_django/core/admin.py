from django.contrib import admin
from .models import Employee,Dept
# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id","name"]


@admin.register(Dept)
class DeptAdmin(admin.ModelAdmin):
    list_display = ["id","name","emps"]
