# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Coach (models.Model):
    user = models.OneToOneField(User)
    bdate = models.DateField()
    gender = models.CharField(max_length=2, choices=(('1', 'Male'), ('2', 'Famale')))
    phone = models.CharField(max_length=13)
    adress = models.CharField(max_length=100)
    skype = models.CharField(max_length=50)
    desc = models.TextField()

    def __unicode__(self):
        return self.user.first_name
