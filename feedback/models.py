# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

class Letter(models.Model):
	name = models.CharField(verbose_name=u'Ваше имя', max_length=255)
	theme = models.CharField(verbose_name=u'Тема сообщения', max_length=255,
							null=False, blank=False)
	body = models.TextField(verbose_name=u'Сообщение', null=False, blank=False)
	email = models.EmailField(verbose_name=u'Ваш Email')
	send_time = models.DateTimeField(verbose_name=u'Время отправки', auto_now_add=True, editable=False)

	def __unicode__ (self):
		return self.name
