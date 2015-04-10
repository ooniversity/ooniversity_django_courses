from django.shortcuts import render
from models import Course

def main(request):
	courses = Course.objects.all()
	return render(request, 'main.html', {'courses': courses})

def course_description(request, course_id):
	course = Course.objects.get(pk = course_id)
	lessons = course.lessons_set.all().order_by('number')	
	return render(request, 'course.html', {'course': course,'lessons': lessons})