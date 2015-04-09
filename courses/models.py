# -*- coding: utf-8 -*-
from django.db import models
from coaches.models import Coach

class Course(models.Model):
    name = models.CharField(u"Название", max_length=255)
    short_description = models.CharField(u"Краткое описание", max_length=255)
    description = models.TextField(u"Описание")
    coach = models.ForeignKey(Coach, verbose_name=u"Тренер", null=True, related_name='coachkey')
    assistant = models.ForeignKey(Coach, verbose_name=u"Ассистент", null=True, related_name='assistantkey')

    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(u"Тема", max_length=255)
    description = models.TextField(u"Описание")
    course = models.ForeignKey(Course, verbose_name=u"Курс", related_name='coursekey')
    order_number = models.PositiveIntegerField(u"Номер по порядку")

    def __unicode__(self):
        return self.subject