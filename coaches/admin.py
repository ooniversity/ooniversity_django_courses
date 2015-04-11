from django.contrib import admin
from coaches.models import Coach
from django.contrib.auth.models import User
# Register your models here.


class CoachAdmin(admin.ModelAdmin):
    search_fields = ['address']
    list_display = ['full_name', 'email', 'skype']
    list_filter = ['gender']


admin.site.register(Coach, CoachAdmin)
