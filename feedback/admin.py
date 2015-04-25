
from django.contrib import admin
from django.db import models
from feedback.models import FeedbackMessage


class FeedbackMessageAdmin(admin.ModelAdmin):

    def time_seconds(self, obj):
        return obj.date.strftime("%d %b %Y, %H:%M")
    
    list_display = ['time_seconds', 'resp_email']
    list_display_links = ['time_seconds', 'resp_email']
    search_fields = ['surname', 'email']


admin.site.register(FeedbackMessage, FeedbackMessageAdmin)
