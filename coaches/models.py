# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Coach (models.Model):
	user = models.OneToOneField(User)  
	birth_date = models.DateField()
	gender = models.CharField(verbose_name=u'Пол', max_length=1, choices=(('M','Male'),('F','Female')))
	phone = models.CharField(verbose_name=u'Телефон', max_length=15)
	adress = models.CharField(verbose_name=u'Адрес',max_length=255)
	skype = models.CharField(verbose_name=u'Skype',max_length=15)
	description = models.TextField(verbose_name=u'О преподавателе', null=True, blank=True)

	def __unicode__ (self):
		full_name = ' '.join([self.user.first_name,self.user.last_name])
		return full_name
