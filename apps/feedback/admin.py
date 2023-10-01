from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("student", "emoji", "message")
    search_fields = ("student", "emoji", "message")
    ordering = ("-created_at",)
    list_filter = ("student", "student__school_class")
