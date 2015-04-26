# ~*~ coding: utf-8 ~*~
from django.db import models
from datetime import datetime

class Mail(models.Model):
    sender_name = models.CharField("Имя отправителя",max_length=100)
    message_theme = models.CharField("Тема сообщения",max_length=100,blank=True, null=True)
    message = models.TextField("Сообщение")
    message_date = models.DateTimeField("Дата создания",blank=True, null=True, default=datetime.now())
    sender_email = models.EmailField("Адрес эл.почты",blank=True, null=True)
    send_date = models.DateTimeField("Дата отправки",blank=True, null=True)

    def __unicode__(self):
        return self.sender_name
    class Meta:
        ordering = ['-message_date']
