from django.db import models
from courses.models import Course, Lesson

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 255)
    surname = models.CharField(max_length = 255)
    birth_date = models.DateField()
    email = models.EmailField()    
    phone = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    scype = models.CharField(max_length = 255)
    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        return self.surname
