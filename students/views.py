from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from courses.models import Courses, Lesson
from students.models import Students

'''
def index(request):
    t = loader.get_template('index.html')
    c = Context({})
    return HttpResponse(t.render(c))
'''

def contact(request):
    t = loader.get_template('contact.html')
    c = Context({})
    return HttpResponse(t.render(c))

def student_list(request):
	if request.GET:
		n = request.GET[u'course_id']
		stud = Students.objects.filter(course = int(n))
		c = { 'stud': stud }
		return render(request, 'student_list.html', c)
	stud = Students.objects.all()
	c = {"stud": stud}
	return render(request, 'student_list.html', c)

def student_detail(request, pk):
	stud = Students.objects.get(id__exact = int(pk))
	c = { "stud": stud }
	return render(request, 'student_detail.html', c)
