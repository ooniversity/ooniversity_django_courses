from django.db import models
from courses.models import Course

class Student(models.Model):
	name = models.CharField(max_length=10)
 	surname = models.CharField(max_length=10)
 	date_birthday = models.DateField()
 	mail = models.EmailField()
 	phone = models.CharField(max_length=20)
 	address = models.CharField(max_length=40)
 	skype = models.CharField(max_length=20)
 	courses = models.ManyToManyField(Course)

 	def __unicode__(self):
 		return self.surname+" "+self.name

 	def fullname(self):
		return ("%s %s" % (self.name, self.surname))	
 
