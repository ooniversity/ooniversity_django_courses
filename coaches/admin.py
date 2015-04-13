from django.contrib import admin
from coaches.models import Coach

class CoachAdmin(admin.ModelAdmin):
    search_fields = ['user', 'email', 'description']
    list_display = ['user', 'description']
    list_filter = ['sex_choices']

admin.site.register(Coach, CoachAdmin)
