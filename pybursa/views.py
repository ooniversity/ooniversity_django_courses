from django.shortcuts import render
from instructors.models import Instructor

def index(request):
	return render(request,'index.html')


def contact(request):
	context = {'var1':"Hello world!"}
	context['var2'] = 'Hello world'
	context['var3'] = ['a', 'b', 'c', 'd']
	context['var4'] = {'some_str':"Hello python!"}
	context['template'] = 'contact.html'

	instructors = Instructor.objects.all()
	context['instructors']=instructors
	return render(request,'contact.html', context)


def student_detail(request):
	return render(request,'student_detail.html')


def student_list(request):
	return render(request,'student_list.html')