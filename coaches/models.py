from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    sex_choices = models.CharField(
        max_length=15, choices=(('male', 'male'), ('female', 'female')))
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255, blank=True)
    skype = models.CharField(max_length=55)
    description = models.TextField()

    def __unicode__(self):
        return unicode(self.user.get_full_name())
