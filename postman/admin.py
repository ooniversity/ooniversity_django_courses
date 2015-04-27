from django.contrib import admin

from postman.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('sender_email', 'created')

admin.site.register(Feedback, FeedbackAdmin)
