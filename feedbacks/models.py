# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class Feedback(models.Model):
    sender_name = models.CharField(verbose_name=u'ИМЯ отправителя', max_length=70)
    sender_email = models.EmailField(verbose_name=u'E-MAIL отправителя')
    mail_theme = models.CharField(verbose_name=u'ТЕМА письма', max_length=150)
    mail_body = models.TextField(verbose_name=u'ТЕКСТ письма', null=True, blank=True)
    mail_datetime = models.DateTimeField(verbose_name=u'Дата и время отправки',
                                         auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.mail_theme
