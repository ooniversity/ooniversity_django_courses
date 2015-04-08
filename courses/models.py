# -*- coding: utf-8 -*-
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Название")
    short_description = models.CharField(max_length=255, verbose_name=u"Краткое описание")
    description = models.TextField(verbose_name=u"Описание")

    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length=255, verbose_name=u"Тема")
    description = models.TextField(verbose_name=u"Описание")
    course = models.ForeignKey('Course', verbose_name=u"Курс")
    order_number = models.PositiveIntegerField(verbose_name=u"Номер по порядку")

    def __unicode__(self):
        return self.subject