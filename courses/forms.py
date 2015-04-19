# -*- coding: utf-8 -*-
from django import forms

from courses.models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        labels = {'name': "Имя",
                  'short_description': "Описание",
                  'description': "Полное описание",
                  'coach': "Преподаватель",
                  'assistant': "Ассистент",
                  }

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required': 'Поле {fieldname} обязательно должно быть заполнено!'.format(
                fieldname=field.label)}
