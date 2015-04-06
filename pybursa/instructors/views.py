from django.shortcuts import render
from instructors.models import Instructor

def instructors_list(requst):
	instructors = Instructor.objects.all()
	return render(requst, "instructors_list.html", 
					{'instructors':instructors})