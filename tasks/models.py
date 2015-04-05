from django.db import models
from students.models import Student

SCORES_CHOICES = (
	(50, '50'),
	(100, '100'),
	(200, '200'),
	(300, '300'),
)

class Task(models.Model):
	title = models.CharField(max_length=100)
	max_score = models.IntegerField(choices=SCORES_CHOICES, default=100)
	deadline = models.DateTimeField()

	def __unicode__(self):
		return self.title


class CompletedTask(models.Model):
	task = models.ForeignKey(Task)
	student = models.ForeignKey(Student)
	score = models.IntegerField(blank=True, null=True)
	finished_date = models.DateTimeField()

	def was_finished_in_time(self):
		return self.finished_date <= self.task.deadline

	was_finished_in_time.boolean = True
	was_finished_in_time.short_description = "Was finished in time?"

	def __unicode__(self):
		return "%s %s comleted %s with score %d" % (self.student.user.first_name, self.student.user.last_name, self.task.title, self.score)