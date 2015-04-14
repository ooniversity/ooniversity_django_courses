# -*- coding: utf-8 -*-

from django.contrib import admin

from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'email']
    list_display = ['full_name', 'email', 'skype']
    list_filter = ['courses']

    # Settings group fields
    fieldsets = [(u'Личная информация', {'fields': ['name', 'surname', 'date_of_birth']}),
                 (u'Контакты', {'fields': ['email', 'phone', 'address', 'skype',]}),
                 (None, {'fields': ['courses']})]

    # Filter courses
    filter_horizontal = ['courses']

    #save_as = True


admin.site.register(Student, StudentAdmin)
