from django.contrib import admin
from models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Main info', {'fields': ['sender_name', 'sender_email', 'theme', 'message']}),
        ('Date info', {'fields': ['date_create'], 'classes': ['collapse']}),
    ]
    list_display = ('sender_email', 'date_create')
    search_fields = ['sender_email']
    list_filter = ['date_create']

admin.site.register(Feedback, FeedbackAdmin)
