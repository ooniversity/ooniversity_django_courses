from django.conf import settings
from django.db import models

class Coach(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    birth_date = models.DateField()
    GENDERS = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=1, default='M', choices=GENDERS)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=75)
    skype = models.CharField(max_length=25)
    description = models.TextField()

    