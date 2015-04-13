from django.shortcuts import render
from courses.models import Course
from coaches.models import Coach

def courses_home_page(request):
	courses = Course.objects.all()
	return render(request, 'index.html', {'courses': courses})

def courses_one_of(request, pk):
	course_one = Course.objects.get(id=pk) #id?
	lessons = course_one.lessons.all()
	trainer = Coach.objects.all().filter(user=course_one.trainer.user)[0]
	assistant = Coach.objects.all().filter(user=course_one.assistant.user)[0]
	return render(request, 'oneofcourse.html', 
		{'course':course_one, 
		'lessons':lessons,
		'trainer':trainer, 
		'assistant':assistant,
		})
