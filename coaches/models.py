from django.db import models
from django.conf import settings


class Coach(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField()
    gen_choices = (('M', 'Male'), ('F', 'Female'))
    gen = models.CharField(max_length = 1, choices=gen_choices, default = 'M')
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=80, null=True, blank=True)
    adress = models.CharField(max_length=80)
    skype = models.CharField(max_length=50)
    description = models.TextField()

    def __unicode__(self):
        return self.skype
