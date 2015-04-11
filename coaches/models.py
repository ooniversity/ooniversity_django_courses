from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Coach(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=((1, 'M'),(2, 'F'),))
    phone = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    scype = models.CharField(max_length = 255)
    description = models.TextField()

    def __unicode__(self):
        #return self.name
        return self.user
