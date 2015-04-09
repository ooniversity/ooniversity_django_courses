from django.conf import settings
from django.db import models


class Coach(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField()
    gender_choises = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=1, choices=gender_choises)
    phone = models.CharField(max_length=18, unique=True)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __unicode__(self):
        return unicode(self.user)
