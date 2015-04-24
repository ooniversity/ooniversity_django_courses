from django.db import models


class Feedback(models.Model):
	name = models.CharField(max_length=30)
	subject = models.CharField(max_length=100)
	text_message = models.TextField()
	mail = models.EmailField()
	send_data = models.DateTimeField('date published', auto_now_add=True)

	def __unicode__(self):
		return self.name