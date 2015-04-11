import datetime

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User)
    birth = models.DateField("Birthday")
    sex = models.CharField("Sex", max_length=2, choices=SEX)
    phone = models.CharField('Phone number',
        unique=True, max_length=12)
    address = models.CharField("Address", help_text='Enter your address', 
        max_length=256)
    skype = models.CharField("Skype", max_length=128)
    descr = models.TextField("Description")

    def __unicode__(self):
        return unicode(self.user)
