from django.conf import settings
from django.db import models

class Coach(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'),('F', 'Female'))) # First element is rendering to DataBase
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.full_name()

    def full_name(self):
        return u"{0} {1}".format(self.user.first_name, self.user.last_name)
