# -*- coding: utf-8 -*-

from django.db import models


class FeedbackMessage(models.Model):
    from_name = models.CharField(max_length=100)
    from_email = models.EmailField()
    when = models.DateTimeField(auto_now_add=True)
    theme = models.CharField(max_length=255)
    message = models.TextField()

    def __unicode__(self):
        return '{0} - {1}'.format(self.when, self.from_email)
