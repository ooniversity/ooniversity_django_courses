from django.db import models
from django.core.urlresolvers import reverse

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)
    body = models.TextField()
    email = models.EmailField()
    date_of_create = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('feedback')
