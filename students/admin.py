# ~*~ coding: utf-8 ~*~

from django.contrib import admin
from django import forms
from django.db import models
from django.forms import widgets,  CheckboxSelectMultiple
from students.models import Student
from courses.models import Course, Lesson





class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                {'fields': ['student_name', 'student_last_name','student_birth']}),
        ('Контактная информация', {'fields': ['student_email', 'student_phone', 'student_addr',
        'student_skype', 'student_course'],'classes': ['extrapretty']}),
    ]
    formfield_overrides = { models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
#    raw_id_fields = ("student_course",)

    list_display = ("_get_full_name", "student_email", "student_skype")
    list_filter = ['student_course']
    search_fields = ['student_last_name', 'student_email']




admin.site.register(Student, StudentAdmin)


