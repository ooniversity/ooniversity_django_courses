from django.contrib import admin
from coaches.models import Coach

class CoachAdmin(admin.ModelAdmin):
    search_fields = ['skype', 'email']
    list_display = ['user','skype']
    list_filter = ['date_of_birth']

admin.site.register(Coach, CoachAdmin)
