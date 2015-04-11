from django.shortcuts import render
from courses.models import Courses, Lesson
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse

# Create your views here.
def index(request):
	cour = Courses.objects.all()
	c = {"cour": cour}
	return render(request, 'index.html', c)

def course_viev(request, pk):
	one_c = Courses.objects.get(id__exact = int(pk))
	lessons = Lesson.objects.filter(course__id__exact = int(pk))
	c = {"course": one_c, "lessons": lessons}
	return render(request, 'course.html', c)
