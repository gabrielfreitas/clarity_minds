from django.contrib import admin
from .models import Teacher, SchoolClass, Student


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)
    autocomplete_fields = ("teachers",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "school_class")
    search_fields = ("name", "email", "school_class")
    ordering = ("name", "email", "school_class")
    list_filter = ("school_class",)
