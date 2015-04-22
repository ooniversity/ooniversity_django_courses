# -*- coding: utf-8 -*-

from django.conf import settings
from django import forms
from students.models import Student


'''
# Widget from admin
class CalendarWidget(forms.TextInput):
    class Media:
        js = ('/admin/jsi18n/',
              settings.STATIC_URL + 'admin/js/core.js',
              settings.STATIC_URL + "admin/js/calendar.js",
              settings.STATIC_URL + "admin/js/admin/DateTimeShortcuts.js")
        css = {
            'all': (
                settings.STATIC_URL + 'admin/css/widgets.css',)
        }

    def __init__(self, attrs={}):
        super(CalendarWidget, self).__init__(attrs={'class': 'vDateField', 'size': '10'})
'''


class CalendarWidget(forms.TextInput):
    class Media:
        js = (
              #settings.STATIC_URL + 'widgets/calendar/dict.js',
              #settings.STATIC_URL + "widgets/calendar/common1.js",
              settings.STATIC_URL + "widgets/calendar/calendar.js",
             )
        css = {
            'all': (
                settings.STATIC_URL + 'widgets/calendar/calendar.css',
                   )
              }

    def __init__(self, attrs={}):
        super(CalendarWidget, self).__init__(attrs={'class': 'date', 'size': '25'})


class StringWidget(forms.TextInput):

    def __init__(self, attrs={}):
        super(StringWidget, self).__init__(attrs={'class': 'vStringField', 'size': '25'})


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'date_of_birth' : CalendarWidget,
            'name' : StringWidget,
            'surname' : StringWidget,
            'email' : StringWidget,
            'phone' : StringWidget,
            'address' : StringWidget,
            'skype' : StringWidget,
        }


