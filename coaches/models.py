from django.db import models
from django.contrib.auth.models import User


class Coach (models.Model):
	user = models.OneToOneField(User)  
	birth_date = models.DateField()
	gender = models.CharField(max_length=1, choices = (('M', 'Male'),('F','Female')))
	phone = models.CharField(max_length=15)
	adress = models.CharField(max_length=255)
	skype = models.CharField(max_length=15)
	description = models.TextField(null=True, blank=True)

	def __unicode__ (self):
		full_name = ' '.join([self.user.first_name,self.user.last_name])
		return full_name






