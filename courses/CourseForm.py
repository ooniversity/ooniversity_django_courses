# coding=utf-8
from django import forms

from courses.models import Course, Lesson


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
