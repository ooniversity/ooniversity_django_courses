# -*- coding: utf-8 -*-

from django import forms

from courses.models import Course, Lesson


# Create form for model Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        widgets = {'description': forms.Textarea}
        help_texts = {'coach': u'Выберите учителя из списка',
                     'assistant': u'Выберите ассистента из списка'}



# Create form for model Lesson

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson

