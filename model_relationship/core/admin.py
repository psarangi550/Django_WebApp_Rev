from django.contrib import admin
from .models import Course, Section, Lecture


# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "slug"]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "order", "course"]


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "order", "code_link", "slug", "section", ]
