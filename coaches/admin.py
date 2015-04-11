from django.contrib import admin
from django.db import models
from django.forms import widgets
from coaches.models import Coach
from django.contrib.auth.models import User



class CoachAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Pesonal Info', {'fields': ['user', 'sex', 'date_of_birth']}),
        ('Contact Info', {'fields': ['phone', 'address', 'skype']}),
        (None, {'fields': ['description']})
    ]
    list_display = ('full_name', 'user', 'skype', 'sex')
    list_filter = ['sex']
    #search_fields = ['user']
    
    

admin.site.register(Coach, CoachAdmin)



