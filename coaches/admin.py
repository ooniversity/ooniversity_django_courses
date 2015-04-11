from django.contrib import admin

from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'skype']
    list_filter = ['sex']
    search_fields = ['user']

admin.site.register(Coach, CoachAdmin)
