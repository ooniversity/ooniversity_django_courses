from django.db import models
from django.contrib.auth.models import User
from coaches.models import Coach


class Course(models.Model):
	title = models.CharField(verbose_name=u'Name', max_length=255)
	short_description = models.CharField(max_length=255)
	description = models.TextField(null=False, blank=False)
	coach = models.ForeignKey(Coach, related_name='coach_on_course', null=True, blank=True ) 
	assistant = models.ForeignKey(Coach, related_name='assistant_on_course', null=True, blank=True) 

	def __unicode__ (self):
		return self.title


class Lesson(models.Model):
	theme = models.CharField(verbose_name=u'Lesson theme', max_length=255)
	description = models.TextField()
	course = models.ForeignKey(Course)
	number = models.PositiveIntegerField()

	def __unicode__ (self):
		return self.theme
		