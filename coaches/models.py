from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=gender_choices)
    phone = models.CharField(max_length=16, null=True, blank=True)
    address = models.CharField(max_length=100)
    skype = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)

