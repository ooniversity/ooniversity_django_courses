from django.db import models


class Feedback(models.Model):
    sender_name = models.CharField(max_length=32)
    sender_email = models.EmailField()
    subject = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
