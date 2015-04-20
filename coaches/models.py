# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    gender_choises = (
        ('M', u'Муж.'),
        ('F', u'Жен.')
    )
    user = models.OneToOneField(User, verbose_name=u'Пользователь')
    date_of_birth = models.DateField(u'Дата рождения')
    gender = models.CharField(u'Пол', max_length=1, choices=gender_choises)
    phone = models.CharField(u'Телефон', max_length=255, unique=True)
    address = models.CharField(u'Адрес', max_length=255)
    skype = models.CharField(u'Скайп', max_length=255, unique=True, blank=True,
        null=True)
    description = models.TextField(u'Описание')

    def __unicode__(self):
        return unicode(self.user)

    def full_name(self):
        name = self.user.get_full_name()
        return  name
    full_name.short_description = u'Полное имя'

    def descr(self):
        return self.description