# -*- coding: utf-8 -*-
from django.db import models
from coaches.models import Coach


class Course(models.Model):
    course_title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=225)
    description = models.TextField(null=True, blank=True)
    coach = models.ForeignKey(Coach, blank=True, null=True, related_name='coach')
    assistant = models.ForeignKey(Coach, blank=True, null=True, related_name='assistant')
    def __unicode__(self):
        return self.course_title
    

class Lesson(models.Model):
    theme = models.CharField(max_length=255)
    desription = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course)
    consecutive_number =  models.PositiveIntegerField()
    def __unicode__(self):
        return self.theme

