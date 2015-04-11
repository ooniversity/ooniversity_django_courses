from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    

    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    theme = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    course = models.ForeignKey(Course)
    item_no = models.PositiveIntegerField()

    def __unicode__(self):
        return self.theme
