from django.contrib import admin
from feedbacks.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_creation')



admin.site.register(Feedback, FeedbackAdmin)