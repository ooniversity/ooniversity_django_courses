from django.contrib import admin
from courses.models import Coach
from courses.models import Courses

class CoachAdmin(admin.ModelAdmin):
    list_display = ['user', 'skype', 'phone']
    list_filter = ['coach_courses', 'assistant_courses']
    search_fields = ['user', 'skype', 'phone', 'adress', 'desc']

admin.site.register(Coach, CoachAdmin)
