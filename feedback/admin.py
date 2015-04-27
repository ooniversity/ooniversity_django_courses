from django.contrib import admin
from feedback.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('email', 'date', )

admin.site.register(Feedback, FeedbackAdmin)
