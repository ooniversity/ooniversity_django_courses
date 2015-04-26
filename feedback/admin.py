from django.contrib import admin
from feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    #list_display = ('email', 'time_created', )
    list_display = ('email', 'date', )
    
    #def time_created(self, obj):
    #    return (str(obj.date) + " " + str(obj.date))

admin.site.register(Feedback, FeedbackAdmin)
