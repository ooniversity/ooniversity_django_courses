from django.contrib import admin
from coaches.models import Coach

class CoachAdmin(admin.ModelAdmin):
	list_display = ['user', 'skype', 'phone']
	list_filter = ['gen']
	search_fields = ['email']


admin.site.register(Coach, CoachAdmin)
