# -*- coding: utf_8 -*-

from django.db import models
from courses.models import Courses

class Students(models.Model):
    first_name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    birdth_date = models.DateField()
    adress = models.CharField(max_length=300)
    email = models.EmailField()
    email.short_description = 'Email'
    skype = models.CharField(max_length=150)
    skype.short_description = 'Skype'
    phone = models.CharField(max_length=150)
    course = models.ManyToManyField(Courses)
    
    def __unicode__(self):
        return self.first_name

    def full_name(self):
        return self.first_name + ' ' + self.surname
    full_name.short_description = 'Имя Фамилия'
    f_name = property(full_name)
