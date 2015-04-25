# -*- coding: utf-8 -*-
from django.db import models

from courses.models import Course


class Student(models.Model):
	name = models.CharField(verbose_name=u'Имя', max_length=255)
	surname = models.CharField(verbose_name=u'Фамилия', max_length=255)
	birth_date = models.DateField(verbose_name=u'Дата рождения')
	email = models.EmailField()
	phone = models.CharField(verbose_name=u'Телефон', max_length=15)
	adress = models.CharField(verbose_name=u'Адрес', max_length=255, null = True, blank=True)
	skype = models.CharField(max_length=15)
	courses = models.ManyToManyField(Course)

	def __unicode__ (self):
		return self.name
