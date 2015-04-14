from django.db import models

from coaches.models import Coach


class Course(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    coach = models.ForeignKey(Coach, related_name='coach', blank=True, null=True)
    assistant = models.ForeignKey(Coach, related_name='assistant', blank=True, null=True)

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    theme = models.CharField(max_length=100)
    description = models.TextField()
    course_id = models.ForeignKey(Course)
    number_order = models.PositiveIntegerField()

    def __unicode__(self):
        return self.theme

    class Meta:
        ordering = ['number_order']

