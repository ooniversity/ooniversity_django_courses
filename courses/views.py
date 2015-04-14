from django.shortcuts import render, get_object_or_404
from courses.models import Course, Lesson


def courses_main(request):
	return render(request, 'courses/courses_main.html', {'courses': Course.objects.all().order_by('id')})	

def course_info(request, course_id):  	
	return render (request, 'courses/course_page.html',
	{'course_id': Course.objects.get(id=course_id).id,
	'course_title': Course.objects.get(id=course_id).title,	
	'course_shortdescription': Course.objects.get(id=course_id).short_description,
	'lessons': Lesson.objects.filter(course__id=course_id).order_by('number'),
	'coach': Course.objects.get(id=course_id).coach,
	'assistant': Course.objects.get(id=course_id).assistant
	}) 
