from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def coach(request, coach_id):
	coach = Coach.objects.get(pk=coach_id)
	trainer_courses = Course.objects.filter(trainer = coach)
	assistant_courses = Course.objects.filter(assistant = coach)
	return render (request, 'coach.html', {'coach': coach, 
					'trainer_courses': trainer_courses, 'assistant_courses':assistant_courses})
