# -*- coding: utf-8 -*-

from django.db import models
import datetime


class Contact(models.Model):
    name = models.CharField(max_length=25)
    subject = models.CharField(max_length=55)
    body = models.TextField(null=True, blank=True)
    email = models.EmailField()
    date = models.DateTimeField(u'Дата создания', blank=False, default=datetime.datetime.now)

    def __unicode__(self):
        return self.name