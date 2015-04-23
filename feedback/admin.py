from django.contrib import admin

from feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['email_sender', 'date_create']
    search_fields = ['name_sender']

admin.site.register(Feedback, FeedbackAdmin)
