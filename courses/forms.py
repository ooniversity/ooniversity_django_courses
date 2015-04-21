# -*- coding: utf-8 -*-

from django import forms
from courses.models import Course, Lesson


class StringWidget(forms.TextInput):

    def __init__(self, attrs={}):
        super(StringWidget, self).__init__(attrs={'class': 'vStringField', 'size': '41'})


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'name' : StringWidget,
            'short_description' : StringWidget,
        }


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        exclude = ['course']
        widgets = {
            'theme' : StringWidget,
        }

