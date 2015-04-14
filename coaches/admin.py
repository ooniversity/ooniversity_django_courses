from django.contrib import admin	
from coaches.models import Coach

class CoachAdmin(admin.ModelAdmin):
    list_display = ['user','skype']
    list_filter = ['gender']
    search_fields = ['user', 'skype']
    



admin.site.register(Coach, CoachAdmin)
