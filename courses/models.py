# ~*~ coding: utf-8 ~*~

from django.db import models


class Course(models.Model):
    course_name = models.CharField("Название",max_length=100,blank=True, null=True)
    course_brief = models.CharField("Краткое описание",max_length=200,blank=True, null=True)
    course_description = models.TextField("Описание курса")
    def __unicode__(self):
        return self.course_name

class Lesson(models.Model):
    lesson_theme = models.CharField("Тема",max_length=100,blank=True, null=True)
    lesson_description = models.TextField("Описание",blank=True, null=True)
    lesson_course = models.ForeignKey('Course',verbose_name="Курс")
    lesson_number = models.PositiveIntegerField("Номер п/п",blank=True, null=True)

    def __unicode__(self):
        return self.lesson_theme
    class Meta:
        unique_together = (("lesson_number", "lesson_course"),)
