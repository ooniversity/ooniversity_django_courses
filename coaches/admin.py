from django.contrib import admin
from coaches.models import Coach
from django.contrib.auth.models import User

class CoachAdmin(admin.ModelAdmin):
	search_fields = ['address']
	list_display = ['fullname', 'email', 'skype']
	list_filter = ['gender']

admin.site.register(Coach, CoachAdmin)