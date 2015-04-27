# -*- coding: utf_8 -*-
from django.db import models


class Feedback(models.Model):
    email = models.EmailField(verbose_name="Email отправителя")
    name = models.CharField(max_length=255, verbose_name="Имя отправителя")
    subject = models.CharField(max_length=255, verbose_name="Тема сообщения")
    message = models.TextField(verbose_name="Текст сообщения")
    date = models.DateTimeField(verbose_name="Дата отправки", auto_now_add=True)

    def __unicode__(self):
        return self.subject

    def send_date(self):
        return self.date.strftime('%d.%m.%Y %H:%M:%S')
    send_date.short_description = 'Дата и время отправки'