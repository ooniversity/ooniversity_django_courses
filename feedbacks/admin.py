from django.contrib import admin

from feedbacks.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_of_create')
    search_fields = ['email']
    list_filter = ['date_of_create']
    save_as = True


admin.site.register(Feedback, FeedbackAdmin)