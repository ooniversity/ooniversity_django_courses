# -*- coding: utf-8 -*-

from django.db import models

from coaches.models import Coach


class Course(models.Model):
    title = models.CharField(verbose_name=u'Название курса', max_length=100)
    short_descript = models.CharField(verbose_name=u'Краткое описание', max_length=255)
    description = models.TextField(verbose_name=u'Описание')

    coach = models.ForeignKey(Coach, verbose_name=u'Тренер', null=True, blank=True,
                                     related_name='coach')
    assistant = models.ForeignKey(Coach, verbose_name=u'Ассистент', null=True, blank=True,
                                         related_name='assistant')

    def __unicode__(self):
        return self.title


class Lesson(models.Model):
    theme = models.CharField(verbose_name=u'Тема', max_length=200)
    description = models.TextField(verbose_name=u'Описание', null=True, blank=True)
    course = models.ForeignKey(Course, verbose_name=u'Курс')
    number = models.PositiveIntegerField(verbose_name=u'№ урока')

    def __unicode__(self):
        return u'{} - {}'.format(self.number, self.theme)

        #return self.theme
        #return u'{} {} - {}'.format(self.number, self.theme, self.course)
