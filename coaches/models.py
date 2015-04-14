from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    user = models.OneToOneField(User, primary_key=True)#, parent_link=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    about = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return unicode(self.user)
    def full_name(self):
        return user.last_name+" "+user.first_name
