from django.db import models

from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=18, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    skype = models.CharField(max_length=255, unique=True)
    course = models.ManyToManyField(Course)
    image = models.ImageField(null=True, blank=True)

    def __unicode__(self):
        return self.surname

    def admin_thumbnail(self):
        if self.image:
            return u'<img src="%s" width="100" />' % (self.image.url)
        else:
            return '(No image)'
    admin_thumbnail.short_description = 'Image'
    admin_thumbnail.allow_tags = True
