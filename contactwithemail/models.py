from django.db import models

class emailmodel(models.Model):
    name = models.CharField(max_length=70)
    email_subject = models.CharField(max_length=70)
    email_content = models.TextField(null=True, blank=True)
    sender_email = models.EmailField(null=True, blank=True)
    date_of_create = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
