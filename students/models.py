from django.db import models

from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    birth_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=100)
    skype = models.CharField(max_length=32)
    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        return "%s %s" % (self.name, self.surname)

    def full_name(self):
        return self.__unicode__()




