from django.db import models
from coaches.models import Coach
from django.core.urlresolvers import reverse


class Course(models.Model):
    name = models.CharField(max_length=75)
    short_description = models.CharField(max_length=100)
    description = models.TextField()
    coach = models.ForeignKey(Coach, related_name='coach', null=True, blank=True)
    assistant = models.ForeignKey(Coach, related_name='assistant', null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):  
        return reverse('courses:course_edit', kwargs={'pk': self.pk})
        

class Lesson(models.Model):
    topic = models.CharField(max_length=75)
    description = models.TextField()
    course = models.ForeignKey(Course)
    number_order = models.PositiveIntegerField()

    def __unicode__(self):
        return self.topic

