# -*- coding: UTF-8 -*-

import datetime
from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'Имя отправителя')
    subject = models.CharField(max_length=100, verbose_name=u'Тема сообщения')
    message = models.TextField(verbose_name=u'Сообщение')
    email = models.EmailField(verbose_name=u'Email отправителя')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата создания')

    def __unicode__(self):
        return self.name

