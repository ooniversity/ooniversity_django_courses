from django.db import models
from courses.models import Course 

class Student(models.Model):
	name = models.CharField(verbose_name="Name", max_length=20)
	surname = models.CharField(verbose_name="Surname", max_length=25)
	birthday = models.DateField(verbose_name="Date of birth")
	email = models.EmailField(verbose_name="E-mail")
	cell = models.CharField(verbose_name="Phone number", max_length=20)
	address = models.CharField(verbose_name="Address", max_length=50, null=True, blank=True)
	skype = models.CharField(verbose_name="Skype", max_length=20, null=True, blank=True)
	courses = models.ManyToManyField(Course)

	def __unicode__(self):
		return self.surname

	def fullname(self):
		return self.name + ' ' + self.surname