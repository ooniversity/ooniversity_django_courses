from django.contrib import admin
from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
	ordering = ('id',)
	list_display = ['user', 'phone']
	search_fields = ['user']
	list_filter = ['sex']
	

admin.site.register(Coach, CoachAdmin)

