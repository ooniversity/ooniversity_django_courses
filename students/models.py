# -*- coding: utf-8 -*-
from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=225)
    surname = models.CharField(max_length=225)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=225)
    skype = models.CharField(max_length=225)
    course = models.ManyToManyField(Course)
    def __unicode__(self):
        return u'{} {}'.format(self.surname, self.name)
    
    
