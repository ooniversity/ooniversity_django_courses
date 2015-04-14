from django.db import models
from coaches.models import Coach

class Course(models.Model):
	name = models.CharField(verbose_name="Name", max_length=30)
	brief = models.CharField(verbose_name="Brief description", max_length=150)
	description = models.TextField(verbose_name="Description", blank=True, null=True)
	teacher = models.ForeignKey(Coach, null=True, blank=True)
	assistant = models.ForeignKey(Coach, related_name='+', null=True, blank=True) 

	def __unicode__(self):
		return self.name

class Lesson(models.Model):
	theme = models.CharField(verbose_name="Theme", max_length=30)
	description = models.TextField(verbose_name="Description", max_length=150)
	course = models.ForeignKey(Course)
	number = models.PositiveIntegerField(verbose_name="Number")

	def __unicode__(self):
		return self.theme