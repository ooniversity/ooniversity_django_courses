from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    courses = models.ManyToManyField('courses.Course')

    def __unicode__(self):
        return u'%s %s' % (self.name, self.surname)

    def full_name(self):
        return self.surname + " " + self.name

