from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=70)
    surname = models.CharField(max_length=70)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    adress = models.CharField(max_length=80)
    skype = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)

    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        return self.name

class CourseApplication(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    courses = models.ForeignKey(Course)
    package = models.CharField(max_length=70, choices=(
        ('standart', "Standart"), ('gold', "Gold"), ('vip', "VIP")))
    comment = models.TextField()
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name