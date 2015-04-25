from django.contrib import admin

from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
	list_display = ['user', 'phone', 'skype']
	search_fields = ['user']
	list_filter = ['gender']	

admin.site.register(Coach, CoachAdmin)
