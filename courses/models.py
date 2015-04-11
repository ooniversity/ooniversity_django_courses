from django.db import models
from coaches.models import Coach

class Course(models.Model):
    name = models.CharField(max_length=70)
    short_description = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    coach = models.ForeignKey(Coach, related_name='coach_courses', null='True', blank='True')
    assist = models.ForeignKey(Coach, related_name='assistant_courses', null='True', blank='True')


    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    theme = models.CharField(max_length=70)
    description = models.TextField(null=True, blank=True)
    number = models.PositiveIntegerField()

    course = models.ForeignKey(Course)

    def __unicode__(self):
        return self.theme

