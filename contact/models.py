from django.db import models


class Contact(models.Model):
    senders_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    senders_email = models.EmailField()
    date_created =  models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.senders_email


