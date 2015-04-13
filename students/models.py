from django.db import models
from courses.models import Course


class Student(models.Model):

 	name = models.CharField(max_length=255)
 	surname = models.CharField(max_length=255)
 	email = models.EmailField()
 	date_of_birth = models.DateField()
 	phone = models.CharField(max_length=255)
 	address = models.CharField(max_length=255)
 	skype = models.CharField(max_length=255)
 	course = models.ManyToManyField(Course, related_name="students")

 	def courses(self):
 		return self.course.all()

 	def full_name(self):
 		return self.name + " " + self.surname

 	def __unicode__(self):
 		return self.name+' '+self.surname


