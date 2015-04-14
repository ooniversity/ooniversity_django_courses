# ~*~ coding: utf-8 ~*~

from django.db import models


class Student(models.Model):
    student_last_name = models.CharField("Фамилия",max_length=30)
    student_name = models.CharField("Имя",max_length=20,blank=True, null=True)
    student_birth = models.DateField("Дата рождения",blank=True, null=True)
    student_email = models.EmailField("Адрес эл.почты",blank=True, null=True)
    student_phone = models.CharField("Телефон",max_length=20,blank=True, null=True)
    student_addr = models.CharField("Почтовый адрес",max_length=50,blank=True, null=True)
    student_skype = models.CharField("Логин Skype",max_length=50,blank=True, null=True)
    student_course = models.ManyToManyField('courses.Course', verbose_name="Курсы")
    def __unicode__(self):
        return self.student_last_name
    def _get_full_name(self):
        return '%s %s' % (self.student_name, self.student_last_name)
    _get_full_name.short_description = 'Студент'
    _get_full_name.admin_order_field = 'student_last_name'

    class Meta:

        unique_together = (("student_last_name", "student_name"),)

        ordering = ['student_last_name']

