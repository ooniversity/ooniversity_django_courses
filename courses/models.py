from django.db import models
from coaches.models import Coach


class Course(models.Model):
    title = models.CharField("Title", help_text="Enter a title of course", 
        max_length=30)
    descr_sm = models.CharField("Small description", max_length=128)
    descr_full = models.TextField("Full description")
    coach = models.ForeignKey(Coach, related_name='coach_n')
    assistant = models.ForeignKey(Coach, related_name='assistant_n')

    def __unicode__(self):
        return self.title


class Lesson(models.Model):
    theme = models.CharField("Theme", max_length=64)
    descr = models.TextField("Description")
    course = models.ForeignKey(Course, related_name='lessons_list')
    num_in_plan = models.PositiveIntegerField(verbose_name=u'Number in plan')

    def __unicode__(self):
        return self.theme
