from django.contrib import admin
from feedbacks.models import MessageFeedback


class MessageFeedbackAdmin(admin.ModelAdmin):
    list_display = ['mailer', 'creation_date']
    search_fields = ['name', 'mailer']
    list_filter = ['creation_date']


admin.site.register(MessageFeedback, MessageFeedbackAdmin)
