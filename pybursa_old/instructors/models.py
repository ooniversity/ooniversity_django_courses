from django.db import models


class Instructor(models.Model):
	name = models.CharField(max_length=255)
	surname = models.CharField(max_length=255)
	date_of_birth = models.DateField()
	email = models.EmailField()
	phone = models.CharField(max_length=15)
	course = models.CharField(max_length=255)