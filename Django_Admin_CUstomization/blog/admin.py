from django.contrib import admin
from .models import Equipment

# Register your models here.


class BlogAdmin(admin.AdminSite):
    site_header = "Blog Admin"


blog_site = BlogAdmin(name="BlogAdmin")

blog_site.register(Equipment)

admin.site.register(Equipment)
