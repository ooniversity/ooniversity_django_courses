from django.contrib import admin

from  feedbacks.models import  Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['email', 'date_of_creation']    
admin.site.register(Feedback, FeedbackAdmin)

