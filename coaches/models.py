from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    sex = models.CharField(
        max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    skype = models.CharField(max_length=30)
    description = models.TextField()

    def __unicode__(self):
        return unicode(self.user)

    def full_name(self):
        name = self.user.get_full_name()
        return name
