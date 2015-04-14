from django.contrib import admin

from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal info', {'fields': ['user', 'date_of_birth', 'gender']}),
        ('Contact info', {'fields': ['phone', 'address', 'skype', 'description']}),
    ]
    list_display = ('full_name', 'email', 'skype')
    search_fields = ['skype']
    list_filter = ['gender']

admin.site.register(Coach, CoachAdmin)
