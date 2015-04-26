# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

class Contact(models.Model):
    your_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    your_email = models.EmailField()
    date =  models.DateTimeField(default=datetime.now, blank=False)

    def __unicode__(self):
        return self.your_email
