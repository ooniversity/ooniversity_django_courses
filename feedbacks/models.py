# -*- coding: utf-8 -*-
from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=225)
    theme = models.CharField(max_length=225)
    message = models.CharField(max_length=225)
    email = models.EmailField()
    date_of_creation = models.DateField(auto_now=True)
    def __unicode__(self):
        return self.name