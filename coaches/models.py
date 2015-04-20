from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
	user = models.OneToOneField(User)
	birthday = models.DateField()
	sex = models.CharField(max_length=20, choices = (('m', "male"), ('f', "female"),))
	phone = models.CharField(max_length=20)
	address = models.CharField(max_length=30)
	skype = models.CharField(max_length=10)
	description = models.TextField(blank=True, null=True)

	def __unicode__(self):
		return self.user.get_full_name()