from django.contrib import admin
from coaches.models import Coach

class CoachAdmin(admin.ModelAdmin):
	search_fields = ['skype']
	list_display = ['user', 'gender', 'skype']
	list_filter = ['gender']

admin.site.register(Coach, CoachAdmin)

