from django.contrib import admin
from django.db import models
from django.forms import widgets
from coaches.models import Coach
from django.contrib.auth.models import User



class CoachAdmin(admin.ModelAdmin):
    #list_display = ['first_name', 'last_name', 'email', 'date_of_birth', ]
    #list_filter = ['']
    #search_fields = ['']
    pass    
    
    

admin.site.register(Coach, CoachAdmin)



