from django.contrib import admin
from django.db import models
from django.forms import widgets
from coaches.models import Coach
from django.contrib.auth.models import User


class UserInline(admin.StackedInline):
    model = User
    extra = 0

class CoachAdmin(admin.ModelAdmin):
    #list_display = ['username', 'first_name', 'last_name', 'email', 'date_of_birth', ]
    #list_filter = ['']
    #search_fields = ['']
    #inlines = [UserInline]
    pass

admin.site.register(Coach, CoachAdmin)



