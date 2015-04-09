from django.contrib import admin
from coaches.models import Coach

class CoachAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name']
    list_filter = ['gender']
    search_fields = ['user']

    fieldsets = [
        ('Pesonal Info', {'fields': ['user', 'gender', 'date_of_birth']}),
        ('Contact Info', {'fields': ['phone', 'address', 'skype']}),
        (None, {'fields': ['description']})
    ]

admin.site.register(Coach, CoachAdmin)
