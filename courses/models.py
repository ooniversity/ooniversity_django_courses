from django.db import models

class Course(models.Model):
     name = models.CharField(max_length=255)
     short_description = models.CharField(max_length=255)
     description = models.TextField()

     def __unicode__(self):
          return self.name

class Lesson(models.Model):
     topic = models.CharField(max_length=85)
     description = models.TextField()
     course = models.ForeignKey(Course)
     index_numer = models.PositiveIntegerField()

     def __unicode__(self):
          return self.topic
