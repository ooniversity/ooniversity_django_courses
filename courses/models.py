from django.db import models

from coaches.models import Coach


class Course(models.Model):
    title = models.CharField(max_length=50)
    comment = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    coach = models.ForeignKey(Coach, related_name='ref_coach', null=True, blank=True)
    assistant = models.ForeignKey(Coach, related_name='ref_assistant', null=True, blank=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ['id']

class Lesson(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course)
    release_num = models.PositiveIntegerField()

    def __unicode__(self):              # __unicode__ on Python 2
        return self.title


