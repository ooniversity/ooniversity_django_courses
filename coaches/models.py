from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=15)
    description = models.TextField()

    def __unicode__(self):
        return u"{0} {1}".format(self.user.first_name, self.user.last_name)
