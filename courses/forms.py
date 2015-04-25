# -*- coding: utf-8 -*-

from django import forms

from courses.models import Course, Lesson


# Create form for model Course

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course

        fields = '__all__'

        widgets = {'description': forms.Textarea}
        help_texts = {'coach': u'Выберите учителя из списка',
                     'assistant': u'Выберите ассистента из списка'}



# Create form for model Lesson

class LessonModelForm(forms.ModelForm):
    class Meta:
        model = Lesson

        fields = '__all__'
