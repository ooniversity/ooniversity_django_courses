from django.db import models
from coaches.models import Coach

# Create your models here.
class Courses(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	text = models.TextField()
	trener = models.ForeignKey(Coach, blank=True, null=True, related_name='coach_courses')
	assist = models.ForeignKey(Coach, blank=True, null=True, related_name='assistant_courses')
	
	def __unicode__(self):
		return self.name
	
class Lesson(models.Model):
	thema = models.CharField(max_length=255)
	text = models.TextField()
	course = models.ForeignKey(Courses)
	num = models.PositiveIntegerField()
	
	def __unicode__(self):
		return self.thema
	

