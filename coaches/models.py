from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(
                             ('F', 'Female'),
                             ('M', 'Male'),))
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=200)
    skype = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u'{0} {1}'.format(self.user.first_name, self.user.last_name)

    def full_name(self):
        return u'{0} {1}'.format(self.user.first_name, self.user.last_name)

    def email(self):
        return self.user.email
