from django.db import models

from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=18, unique=True)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255, unique=True)
    course = models.ManyToManyField(Course)

    def __unicode__(self):
        return self.surname
