from django.db import models
from coaches.models import Coach
from django.core.urlresolvers import reverse


# Create your models here.
class Course(models.Model):

    name = models.CharField(max_length = 255)
    short_description = models.CharField(max_length = 250)
    description = models.TextField()

    trainer = models.ForeignKey(
        Coach, related_name = "rel_trainers", 
        blank = True, null = True)

    assistant = models.ForeignKey(
        Coach, related_name = "rel_assistants", 
        blank = True, null = True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('courses:course_edit', kwargs={'pk': self.pk})

class Lesson(models.Model):
    topic = models.CharField(verbose_name=u'Subject', max_length = 255)
    description = models.TextField(max_length = 500)
    course = models.ForeignKey(Course)
    index = models.PositiveIntegerField(verbose_name=u'Order')

    def __unicode__(self):
        return self.topic
