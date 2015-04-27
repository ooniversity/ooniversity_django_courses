from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse


class Feedback(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField(max_length=100)
    theme = models.CharField(max_length=100)
    message = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.theme

    def get_absolute_url(self):
        return reverse('feedback')




