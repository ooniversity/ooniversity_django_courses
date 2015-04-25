from django.db import models
from datetime import datetime


class Feedback(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField(max_length=100)
    theme = models.CharField(max_length=100)
    message = models.TextField()
    date_create = models.DateTimeField(default=datetime.now(),blank=True)

    def __unicode__(self):
        return self.theme


