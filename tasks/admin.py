from django.contrib import admin
from .models import Task, CompletedTask

class CompletedTaskAdmin(admin.ModelAdmin):
	list_display = ('task', 'student', 'was_finished_in_time', 'score')
	list_filter = ['task', 'student']
	search_fields = ['student']

admin.site.register(Task)
admin.site.register(CompletedTask, CompletedTaskAdmin)

