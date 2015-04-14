from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
	user = models.OneToOneField(User)
	date_of_birth = models.DateField()
	gender = models.CharField(max_length=1, choices = (("M", "Male"),("F", "Female")))
	phone = models.CharField(max_length=10)
	address = models.CharField(max_length=255, default="")
	skype = models.CharField(max_length=255)
	description = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return unicode(self.user)

	def full_name(self):
		n = self.user.get_full_name()
		return n