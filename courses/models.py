from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    short_descript = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return self.title


class Lesson(models.Model):
    theme = models.CharField(max_length=200)
    description = models.TextField()
    course = models.ForeignKey(Course)
    number = models.PositiveIntegerField()

    def __unicode__(self):
        return u'{} - {}'.format(self.number, self.theme)

        #return self.theme
        #return u'{} {} - {}'.format(self.number, self.theme, self.course)
