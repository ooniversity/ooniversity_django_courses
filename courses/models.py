from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=1000)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    theme = models.CharField(max_length=200)
    description = models.TextField()
    course = models.ForeignKey(Course)
    number = models.PositiveIntegerField()

    def __unicode__(self):
        return self.theme
