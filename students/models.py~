from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    adress = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    course = models.ManyToManyField(Course)

    def name_surname(self):
        return self.name + ' ' + self.surname

    def __unicode__(self):
        return self.name_surname()
