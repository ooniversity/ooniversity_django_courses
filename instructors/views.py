from django.shortcuts import render
from instructors.models import Instructor

def instructors_list(request):
	instructors = Instructor.objects.filter(is_active=True)
	return render(request, 'instructors_list.html', 
					{'instructors': instructors})