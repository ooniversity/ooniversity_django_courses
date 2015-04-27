from django.contrib import admin

from feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('senders_email', 'created')
    search_fields = ['senders_email']
    list_filter = ['created']
    save_as = True


admin.site.register(Feedback, FeedbackAdmin)