 #-*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Coach (models.Model):
    user = models.OneToOneField(User)
    photo = models.ImageField(upload_to='static/images/Coaches/', verbose_name=u'Фото',null=True, blank=True)
    date_of_birth = models.DateField(verbose_name='Birth date')
    gender = models.CharField(verbose_name='Gender', max_length=1,
                              choices=(('M', 'Man'), ('W', 'Woman')))
    phone = models.CharField(verbose_name='Phone number', max_length=15)
    address = models.CharField(verbose_name='Address', max_length=50, null=True,
                              blank=True)
    skype = models.CharField(verbose_name='Skype', max_length=50, null=True,
                            blank=True)
    discription = models.TextField(verbose_name='Coach discription', null=True,
                                  blank=True)

    def __unicode__(self):
        return u'{} {}'.format(self.user.last_name, self.user.first_name)

    def full_name(self):
        return u'{} {}'.format(self.user.last_name, self.user.first_name)

    def surname(self):
        return self.user.last_name

    def email(self):
        return self.user.email
