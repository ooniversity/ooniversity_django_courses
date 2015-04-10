from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=75)
    short_description = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name
        
class Lesson(models.Model):
    topic = models.CharField(max_length=75)
    description = models.TextField()
    course = models.ForeignKey(Course)
    number_order = models.PositiveIntegerField()

    def __unicode__(self):
        return self.topic

