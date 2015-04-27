# -*- coding: utf-8 -*-
from django.contrib import admin
from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'skype']
    search_fields = ['surname', 'email']
    list_filter = ['course']

# Settings group fields
fieldsets = [(u'Личная информация', {'fields': ['name', 'surname', 'date_of_birth']}),
(u'Контакты', {'fields': ['email', 'phone', 'address', 'skype',]}),
(None, {'fields': ['courses']})]
# Filter courses
filter_horizontal = ['courses']

    
admin.site.register(Student, StudentAdmin)
