# ~*~ coding: utf-8 ~*~
from django.contrib import admin
from coaches.models import Coach
from django.contrib.auth.models import User
from courses.models import Course



class CoachAdmin(admin.ModelAdmin):

    list_display = ( "coach_user", "coach_birth", "coach_description")
    list_filter = ['coach_sex']
    search_fields = ['coach_user']

admin.site.register(Coach, CoachAdmin )

