# -*- coding: utf-8 -*-
from django.db import models


class Feedback(models.Model):
    sender = models.CharField(u"Имя отправителя", max_length=100)
    subject = models.CharField(u"Тема", max_length=300)
    senders_email = models.EmailField(u"Адрес отправителя")
    message = models.TextField(u"Сообщение", max_length=1000)
    created = models.DateTimeField(u"Созданно:", auto_now_add=True, blank=True)

