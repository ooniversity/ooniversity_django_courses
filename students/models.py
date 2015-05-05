from django.db import models
from courses.models import Course


#class Adress(models.Model):
    #city = models.CharField(max_length=21)
    #other = models.CharField(max_length=21)

class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Student name', help_text='This is name')
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course)

    def my_property(self):
        return self.name + ' ' + self.surname

    full_name = property(my_property)
