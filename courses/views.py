from django.shortcuts import render
from courses.models import Course

def courses_home_page(request):
	courses = Course.objects.all()
	return render(request, 'index.html', {'courses': courses})

def courses_one_of(request, pk):
	course_one = Course.objects.get(pk=pk)
	lessons = course_one.lessons.all()
	return render(request, 'oneofcourse.html', {'course':course_one, 'lessons':lessons})
