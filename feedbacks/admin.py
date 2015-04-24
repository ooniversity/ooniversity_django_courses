from django.contrib import admin
from feedbacks.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
	list_display = ['mail', 'send_data']	


admin.site.register(Feedback, FeedbackAdmin)


