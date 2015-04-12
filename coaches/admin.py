from django.contrib import admin
from django.db import models
from django.forms import widgets
from coaches.models import Coach
from django.contrib.auth.models import User


class CoachAdmin(admin.ModelAdmin):
    readonly_fields = ('user_email', 'user_first_name', 'user_last_name')
    fieldsets = [
        ('Pesonal Info', {'fields': ['user', 'user_first_name', 'user_last_name', 'sex', 'date_of_birth']}),
        ('Contact Info', {'fields': ['user_email', 'phone', 'address', 'skype']}),
        (None, {'fields': ['description']})
    ]
    list_display = ('full_name', 'user', 'skype', 'sex')
    list_filter = ['sex']
    search_fields = ['user__first_name', 'user__last_name', 'user__username']
    

admin.site.register(Coach, CoachAdmin)



