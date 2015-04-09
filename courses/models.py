# -*- coding: utf-8 -*-
from django.db import models

class Course(models.Model):
    name = models.CharField(u"Название", max_length=255)
    short_description = models.CharField(u"Краткое описание", max_length=255)
    description = models.TextField(u"Описание")

    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(u"Тема", max_length=255)
    description = models.TextField(u"Описание")
    course = models.ForeignKey('Course', verbose_name=u"Курс", related_name='coursekey')
    order_number = models.PositiveIntegerField(u"Номер по порядку")

    def __unicode__(self):
        return self.subject