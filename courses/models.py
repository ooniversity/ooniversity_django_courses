from django.db import models


class Course(models.Model):
	title = models.CharField(verbose_name=u'Name', max_length=255)
	short_description = models.CharField(max_length=255)
	description = models.TextField(null=False, blank=False)

	def __unicode__ (self):
		return self.title


class Lesson(models.Model):
	theme = models.CharField(verbose_name=u'Lesson theme', max_length=255)
	description = models.TextField()
	course = models.ForeignKey(Course)
	number = models.PositiveIntegerField()

	def __unicode__ (self):
		return self.theme