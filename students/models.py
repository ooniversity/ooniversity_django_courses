# -*- coding: utf-8 -*-
from django.db import models
from courses.models import Course
# Create your models here.


class Student (models.Model):
    name = models.CharField(verbose_name='Name', max_length=15)
    surname = models.CharField(verbose_name='Surname', max_length=30)
    date_of_birth = models.DateField(verbose_name='Birth date')
    email = models.EmailField(verbose_name='E-mail')
    phone = models.CharField(verbose_name='Phone number', max_length=15)
    address = models.CharField(verbose_name='Address', max_length=50, null=True, blank=True)
    skype = models.CharField(verbose_name='Skype', max_length=50, null=True, blank=True)
    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        return self.surname


    def full_name(self):
        return " ".join([self.name, self.surname])

