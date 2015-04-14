from django.contrib import admin

from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    search_fields = ['user']
    list_display = ('user', 'gender', 'skype')


admin.site.register(Coach, CoachAdmin)
