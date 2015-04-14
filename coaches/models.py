from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField('Birthday')
    sex = models.CharField(max_length=1, choices=(
        ('M', 'Male'), ('F', 'Female'))
    )
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100)
    skype = models.CharField(max_length=25)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.user.get_full_name()