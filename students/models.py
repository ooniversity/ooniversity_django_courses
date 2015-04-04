from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
	user = models.OneToOneField(User)
	skype = models.CharField(max_length=30, blank=True, null=True)
	address = models.CharField(max_length=150, blank=True, null=True)
	date_of_birth = models.DateField()

	def get_average_score(self, *args, **kwargs):
		completed_tasks = self.completedtask_set.all()
		tasks_count = completed_tasks.count()
		total_score = sum([task.score for task in completed_tasks])
		av_score = total_score/tasks_count if tasks_count > 0 else 0
		return av_score
		
	def __unicode__(self):
		return "%s %s" % (self.user.first_name, self.user.last_name)
