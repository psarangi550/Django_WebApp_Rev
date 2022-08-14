from django.contrib import admin
from .models import Book


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug", "author", "genre", "create_at", "updated_at"]
    prepopulated_fields = {"slug": ("name",)}
