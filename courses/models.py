from django.db import models
from django.forms import ModelForm, widgets
from django import forms

from coaches.models import Coach


class Course(models.Model):
    title = models.CharField(
        "Title", help_text="Enter a title of course",
        max_length=30)
    descr_sm = models.CharField("Small description", max_length=128)
    descr_full = models.TextField("Full description")
    coach = models.ForeignKey(
        Coach, blank=True, null=True,
        related_name='courses_as_coach')
    assistant = models.ForeignKey(
        Coach, blank=True, null=True,
        related_name='courses_as_assistant')

    def __unicode__(self):
        return self.title


class CourseForm(ModelForm):
    class Meta:
        model = Course
        widgets = {
            'coach': forms.Select,
            'assistant': forms.Select,
        }
        labels = {
            'descr_sm': 'Description short',
            'descr_full': 'Description full',
        }
        fields = '__all__'


class Lesson(models.Model):
    theme = models.CharField("Theme", max_length=64)
    descr = models.TextField("Description")
    course = models.ForeignKey(Course, related_name='lessons_list')
    num_in_plan = models.PositiveIntegerField(verbose_name=u'Number in plan')

    def __unicode__(self):
        return self.theme


class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        widgets = {
            'course': forms.Select,
        }
        labels = {
            'descr': 'Description',
            'num_in_plan': 'Number in plan'
        }
        fields = '__all__'

