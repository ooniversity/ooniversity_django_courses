from django.db import models
from courses.models import Course, Lesson
from django.core.urlresolvers import reverse

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 255)
    surname = models.CharField(max_length = 255)
    birth_date = models.DateField()#YYYY-MM-DD
    email = models.EmailField()    
    phone = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    scype = models.CharField(max_length = 255)
    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        return self.surname
    """
    def __unicode__(self):
        return ('INFO ON A STUDENT:\n%s %s,\nbirth date: %s,\nemail: %s,\nphone: %s,\naddress: %s,\nskype: %s'
                %
                (self.surname, self.name, 
                str(self.birth_date), 
                self.email, self.phone,
                self.address, self.scype))
    """

    def get_absolute_url(self):
        return reverse('students:student_edit', kwargs={'pk': self.pk})
