from django.db import models
from django.core.urlresolvers import reverse

class MessageFeedback(models.Model):
    name = models.CharField(max_length=100)
    theme = models.CharField(max_length=255)
    message = models.TextField()
    mailer = models.EmailField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


   # def get_absolute_url(self):
   #     return reverse('feedback')

