from django.db import models

# Create your models here.

from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=70)
    surname = models.CharField(max_length=70)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=80)
    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        return self.name
