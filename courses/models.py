from django.db import models
from coaches.models import Coach

class Course(models.Model):
    title = models.CharField(max_length=255)
    descr = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(Coach, related_name='+', blank=True, null=True)
    assistant = models.ForeignKey(Coach, related_name='+', blank=True, null=True)
    def __unicode__(self):
        return self.title


class Lesson(models.Model):
    theme = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey('Course')
    serial = models.PositiveIntegerField()
    def __unicode__(self):
        return self.theme



