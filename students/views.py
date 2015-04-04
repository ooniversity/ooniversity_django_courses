from django.shortcuts import render_to_response
from django.views import generic
from .models import Student

class StudentListView(generic.ListView):
	model = Student
	context_object_name = 'students'

def  dummy_render(request, pk=0, template="students/student_list.html"):
	return render_to_response(template)
