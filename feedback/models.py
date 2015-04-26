from django.db import models
from django.forms import ModelForm
from django import forms
from django.utils import timezone #see turorial - polls app

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    message = models.TextField()
    email = models.EmailField()    
    #date = models.DateField(auto_now_add=True)
    #date = models.DateField('date created', auto_now_add=True)
    date = models.DateTimeField('date, time created', auto_now_add=True)

    def __unicode__(self):
        return self.name

    #def get_absolute_url(self):
    #    return reverse('feedback:feedback')
