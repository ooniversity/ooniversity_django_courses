from django.db import models
from coaches.models import Coach

class Course(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=55)
    description = models.TextField(null=True, blank=True)
    instructor = models.ForeignKey(Coach, related_name='instructor', blank=True, null=True)
    assistant = models.ForeignKey(Coach, related_name='assistant', blank=True, null=True)

    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    theme = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course)
    number = models.PositiveIntegerField()

    def __unicode__(self):
        return self.theme
