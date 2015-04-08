from django.contrib import admin
from django.db import models
from django.forms import widgets
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'skype']
    list_display_links = ['full_name']
    search_fields = ['surname', 'email']
    list_filter = ['courses']
    fieldsets = [
        ('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
        (None, {'fields': ['courses']}),
    ]
    filter_horizontal = ['courses']

admin.site.register(Student, StudentAdmin)
