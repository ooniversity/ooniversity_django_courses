from django.db import models
from courses.models import Course


class Student(models.Model):
	name = models.CharField(verbose_name=u'Student name', max_length=255)
	surname = models.CharField(max_length=255)
	birth_date = models.DateField()
	email = models.EmailField()
	phone = models.CharField(max_length=15)
	adress = models.CharField(max_length=255)
	skype = models.CharField(max_length=15)
	courses = models.ManyToManyField(Course)

	def __unicode__ (self):
		return self.name
