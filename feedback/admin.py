from django.contrib import admin

from feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['sender_email', 'create_at']
    search_fields = ['sender_name']

admin.site.register(Feedback, FeedbackAdmin)
