# -*- coding: utf-8 -*-

from django.db import models

from courses.models import Course


class Student(models.Model):
    name = models.CharField(verbose_name=u'Имя', max_length=70)
    surname = models.CharField(verbose_name=u'Фамилия', max_length=70)
    date_of_birth = models.DateField(verbose_name=u'Дата рождения')
    email = models.EmailField(verbose_name='E-mail')
    phone = models.CharField(verbose_name=u'Телефон', max_length=15)
    address = models.CharField(verbose_name=u'Адрес', max_length=255)
    skype = models.CharField(verbose_name='Skype', max_length=80)
    courses = models.ManyToManyField(Course, verbose_name=u'Курсы')

    def __unicode__(self):
        return u'{} {}'.format(self.name, self.surname)


    def full_name(self):
        # (verbose_name = u'Полное имя')
        return (self.name + ' ' + self.surname)
