from django.db import models
from datetime import datetime

class Mail(models.Model):
	name = models.CharField(verbose_name="Sender name", max_length=20)
	subject = models.CharField(verbose_name="Theme", max_length=25)
	message = models.TextField(verbose_name="Message", blank=True, null=True)
	email = models.EmailField(verbose_name="E-mail")
	mail_date = models.DateTimeField(verbose_name="Date sent", editable=False)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.mail_date = datetime.today()
		return super(Mail, self).save(*args, **kwargs)