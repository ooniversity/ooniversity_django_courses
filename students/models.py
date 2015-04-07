import datetime

from django.db import models
from django.utils import timezone
from courses.models import Course


class Student(models.Model):
    name = models.CharField("Name", max_length=25)
    surname = models.CharField("Surname", max_length=25)
    birthday = models.DateField("Birthday")
    email = models.EmailField("Email", unique=True)
    phone_num = models.CharField("Phone number", unique=True, max_length=12)
    address = models.CharField("Address", max_length=256)
    skype = models.CharField("Skype", max_length=128)
    courses = models.ManyToManyField(Course)
