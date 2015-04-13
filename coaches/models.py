# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Coach(models.Model):
    user = models.OneToOneField(User, verbose_name = 'User')
    date_of_birth = models.DateField(verbose_name = u'Дата рождения')

    gender = models.CharField(verbose_name = u'Пол', max_length = 1,
                              choices = (('X', u'мужской'), ('Y', u'женский'))
)
    phone = models.CharField(verbose_name = u'Телефон', max_length = 15)
    address = models.CharField(verbose_name = u'Адрес', max_length = 255)
    skype = models.CharField(verbose_name = 'Skype', max_length = 80)
    description = models.TextField(verbose_name = u'Описание')

    def __unicode__(self):
        return self.user.first_name


    # Functions get personal data users

    def user_name(self):
        return self.user.username

    def full_name(self):
        return u'{} {}'.format(self.user.first_name, self.user.last_name)

    def user_email(self):
        return self.user.email
