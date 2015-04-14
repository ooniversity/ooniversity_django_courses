from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
	user = models.OneToOneField(User)
	birthday = models.DateField(verbose_name='Date of birth')
	gender = models.CharField(verbose_name='Gender', max_length=1,
							  choices=(('M', "Male"), ('F', 'Female')))
	cell = models.CharField(verbose_name='Phone number', max_length=20)
	address = models.CharField(verbose_name='Address', max_length=50, null=True, blank=True)
	skype = models.CharField(verbose_name='Skype', max_length=50, null=True, blank=True)
	description = models.TextField(verbose_name='About coach', null=True, blank=True)

	def __unicode__(self):
		return self.user.last_name + ' ' + self.user.first_name

	def fullname(self):
		return self.user.last_name + ' ' + self.user.first_name

	def email(self):
		return self.user.email
