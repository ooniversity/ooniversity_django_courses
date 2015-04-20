#-*- coding: utf-8 -*-

from django.db import models
from coaches.models import Coach


class Course(models.Model):
    title = models.CharField(max_length=70)
    about = models.CharField(max_length=300)
    more_info = models.TextField()
    coach = models.ForeignKey(
        Coach, blank=True, null=True, related_name='courses_coach')
    assistant = models.ForeignKey(
        Coach, blank=True, null=True, related_name='courses_assistant')

    def __unicode__(self):
        return self.title


class Lesson(models.Model):
    theme = models.CharField(max_length=100)
    about = models.TextField()
    course = models.ForeignKey(Course)
    num = models.PositiveIntegerField(help_text="уроки с номерами ниже уже существуют")

    def __unicode__(self):
        return self.theme
