from django.db import models

from courses.models import Course

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    adress = models.CharField(max_length=200)
    skype = models.CharField(max_length=200)
    course = models.ManyToManyField(Course)
