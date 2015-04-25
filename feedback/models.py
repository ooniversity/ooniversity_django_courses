# -*- coding: utf-8 -*-

from django.db import models


class FeedbackMessage(models.Model):
    mailer = models.CharField(max_length=70, verbose_name="Ваше имя")
    resp_email = models.EmailField(verbose_name="Ваша почта")
    date = models.DateTimeField(auto_now_add=True)
    theme = models.CharField(max_length=255, verbose_name="Тема")
    message = models.TextField(verbose_name="Сообщение")

    def __unicode__(self):
        return '{0}| {1}'.format(self.date, self.resp_email)