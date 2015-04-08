# -*- coding: utf-8 -*-
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    surname = models.CharField(max_length=255, verbose_name=u"Фамилия")
    date_of_birth = models.DateField(verbose_name=u"Дата рождения")
    email = models.EmailField(verbose_name=u"Эл. почта")
    phone = models.CharField(max_length=255, verbose_name=u"Телефон")
    address = models.CharField(max_length=255, verbose_name=u"Адрес")
    skype = models.CharField(max_length=255, verbose_name=u"Скайп")
    courses = models.ManyToManyField('courses.Course')

    def __unicode__(self):
        return '%s %s' % (self.name, self.surname)