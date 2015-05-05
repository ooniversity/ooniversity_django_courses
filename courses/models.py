# -*- coding: utf-8 -*-
from django.db import models
from coaches.models import Coach


class Course(models.Model):
    course_title = models.CharField(verbose_name=u'Название курса', max_length=255)
    short_description = models.CharField(verbose_name=u'Краткое описание', max_length=225)
    description = models.TextField(verbose_name=u'Описание', null=True, blank=True)
    coach = models.ForeignKey(Coach, verbose_name=u'Преподаватель', blank=True, null=True, related_name='coach')
    assistant = models.ForeignKey(Coach, verbose_name=u'Ассистент', blank=True, null=True, related_name='assistant')
    def __unicode__(self):
        return self.course_title
    

class Lesson(models.Model):
    theme = models.CharField(verbose_name=u'Тема', max_length=255)
    desription = models.TextField(verbose_name=u'Описание', null=True, blank=True)
    course = models.ForeignKey(Course, verbose_name=u'Курс')
    consecutive_number =  models.PositiveIntegerField(verbose_name=u'№ занятия')
    def __unicode__(self):
        return u'{} - {}'.format(self.consecutive_number, self.theme)

