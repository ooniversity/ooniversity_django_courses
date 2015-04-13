from django.db import models
from coaches.models import Coach

class Course(models.Model):

	name = models.CharField(max_length=255)
	short_description = models.CharField(max_length=255)
	description = models.TextField(null=True, blank=True)
	trainer = models.ForeignKey(Coach, related_name="trainers", null=True, blank=True)
	assistant = models.ForeignKey(Coach, related_name="assistants", null=True, blank=True)	

	def __unicode__(self):
		return self.name

class Lesson(models.Model):

	theme = models.CharField(max_length=255)
	description = models.TextField(null=True, blank=True)
	course = models.ForeignKey(Course, related_name="lessons")
	num = models.PositiveIntegerField()

	def __unicode__(self):
		return self.theme