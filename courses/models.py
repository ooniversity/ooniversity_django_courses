from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    descr = models.CharField(max_length=255)
    description = models.TextField()
    def __unicode__(self):
        return self.title


class Lesson(models.Model):
    theme = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey('Course')
    serial = models.PositiveIntegerField()
    def __unicode__(self):
        return self.theme
    


