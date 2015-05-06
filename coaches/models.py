# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User



class Coach(models.Model):
    user = models.OneToOneField(User, verbose_name='User')
    date_of_birth = models.DateField(verbose_name=u'Дата рождения')
    gender = models.IntegerField(verbose_name=u'Пол', max_length=1, default=1, choices=((1, 'М'), (2, 'Ж')))
    phone = models.CharField(verbose_name=u'Телефон', max_length=13)
    address = models.CharField(verbose_name=u'Адрес', max_length=225)
    skype = models.CharField(verbose_name='Skype', max_length=225)    
    description = models.TextField(verbose_name=u'Описание', null=True, blank=True)
    
    def __unicode__(self):
        return self.user.first_name

  # Get  data users
    def user_name(self):
        return self.user.username

    def full_name(self):
        return u'{} {}'.format(self.user.first_name, self.user.last_name)
        
    def user_email(self):
        return self.user.email