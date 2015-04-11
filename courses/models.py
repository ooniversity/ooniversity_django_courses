from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=70)
    about = models.CharField(max_length=300)
    more_info = models.TextField()

    def __unicode__(self):
        return self.title

class Lesson(models.Model):
    theme = models.CharField(max_length=100)
    about = models.TextField()
    course = models.ForeignKey(Course)
    num = models.PositiveIntegerField()

    def __unicode__(self):
        return self.theme
