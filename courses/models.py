from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=250)
    description = models.TextField()

class Lesson(models.Model):
    theme = models.CharField(max_length=100)
    description = models.TextField()
    course_id = models.ForeignKey(Course)
    number_order = models.PositiveIntegerField()
