# -*- coding: utf-8 -*-
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    def __unicode__(self):
        return self.last_name


class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.IntegerField(max_length=1, default=1, choices=((1, 'М'), (2, 'Ж')))
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=225)
    skype = models.CharField(max_length=225)    
    description = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return unicode(self.user)

def full_name(self):
    return u'{} {}'.format(self.user.first_name, self.user.last_name)
    
