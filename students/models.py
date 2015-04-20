from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=70)
    surname = models.CharField(max_length=70)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    skype = models.CharField(max_length=30, null=True, blank=True)
    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        return self.name
