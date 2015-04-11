from django.db import models

class Course(models.Model):
	name = models.CharField(max_length=255)
	short_description = models.CharField(max_length=255)
	description = models.TextField()

	def __unicode__(self):
		return self.name


class Lesson(models.Model):
	theme = models.CharField(max_length=255)
	description = models.TextField()
	course= models.ForeignKey(Course, null=True)
	order_number = models.PositiveIntegerField()


	def __unicode__(self):
		return self.theme



