from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length = 255)
    short_description = models.CharField(max_length = 250)
    description = models.CharField(max_length = 500)

    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    topic = models.CharField(max_length = 255)
    description = models.CharField(max_length = 500)
    course = models.ForeignKey(Course)
    index = models.PositiveIntegerField()

    def __unicode__(self):
        return self.topic
