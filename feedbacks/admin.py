from django.contrib import admin

from feedbacks.models import Feedback

# Register your models here.


class FeedbackAdmin(admin.ModelAdmin):

    list_display = ['sender_email', 'mail_datetime']


admin.site.register(Feedback, FeedbackAdmin)
