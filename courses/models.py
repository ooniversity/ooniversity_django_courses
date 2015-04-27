from django.db import models
from django.core.urlresolvers import reverse
from coaches.models import Coach


class Course(models.Model):
	name = models.CharField(max_length=30)
	short_description = models.CharField(max_length=100)
	description = models.TextField()
	trainer = models.ForeignKey(Coach, related_name='trainer', blank=True, null=True)
	assistant = models.ForeignKey(Coach, related_name='assistant', blank=True, null=True)

	def __unicode__(self):
		return self.name


class Lessons(models.Model):
	theme = models.CharField(max_length=40)
	description = models.TextField()
	course = models.ForeignKey(Course)
	number = models.PositiveIntegerField()

	def __unicode__(self):
		return self.theme

			




		


