from django.contrib import admin
from coaches.models import Coach

class CoachAdmin(admin.ModelAdmin):
    list_display = ['user', 'description']
    search_fields = ['user']
    list_filter = ['sex']

    fieldsets = [
        ('Pesonal Info', {'fields': ['user', 'sex', 'date_of_birth']}),
        ('Contact Info', {'fields': ['phone', 'address', 'skype']}),
        (None, {'fields': ['description']})
    ]

admin.site.register(Coach, CoachAdmin)