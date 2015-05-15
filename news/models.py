 #-*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils import timezone


class New (models.Model):
    title = models.CharField(verbose_name=u'Заголовок', max_length=55)
    photo = models.ImageField(upload_to='static/images/News/', verbose_name=u'Фото',null=True, blank=True)
    text = models.TextField(verbose_name=u'Описание', null=True, blank=True)
    date_public = models.DateTimeField(verbose_name=u'Время создания', editable=True, auto_now=True, auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
