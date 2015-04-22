from django.contrib import admin
from django.db import models
from feedback.models import FeedbackMessage


class FeedbackMessageAdmin(admin.ModelAdmin):
    list_display = ['when', 'from_email']
    list_display_links = ['when', 'from_email']
    search_fields = ['surname', 'email']


admin.site.register(FeedbackMessage, FeedbackMessageAdmin)
