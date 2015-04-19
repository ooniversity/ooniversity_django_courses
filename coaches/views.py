from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course

def allcoaches(request):
	coach = Coach.objects.all()
	return render(request, 'coaches.html', {'coach':coach})

def onecoach(request, pk):
	coach = Coach.objects.get(id=pk)
	trainer_courses = Course.objects.filter(trainer=coach)
	assistant_courses = Course.objects.filter(assistant=coach)
	return render(request, 'oneofcoach.html', {'coach':coach, 'trainer_courses':trainer_courses, 'assistant_courses':assistant_courses})
