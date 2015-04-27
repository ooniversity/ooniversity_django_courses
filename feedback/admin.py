from django.contrib import admin
from feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email')
    list_display = ['subject', 'name', 'email', 'send_date']
    list_filter = ['date']


admin.site.register(Feedback, FeedbackAdmin)
