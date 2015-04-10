import datetime
from courses.models import Course

from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=75)
    skype = models.CharField(max_length=25)
    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        return self.name