# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.utils import timezone

class Mail (models.Model):
    name_sender = models.CharField(verbose_name=u'Отправитель', max_length=30)
    subject = models.CharField(verbose_name=u'Тема', max_length=100)
    mail_text = models.TextField(verbose_name=u'Содержание', null=True, blank=True)
    address_sender = models.EmailField(verbose_name=u'E-mail отправителя')
    mail_date = models.DateTimeField(verbose_name=u'Время создания письма', editable=False)
    #default=timezone.now()

    def save(self, *args, **kwargs):
        self.mail_date = datetime.datetime.today()
        return super(Mail, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name_sender
