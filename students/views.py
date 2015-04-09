from django.shortcuts import render
from models import Student
from courses.models import Course

def list_students(request):
	if request.GET.get('course_id'):
		course_id = request.GET['course_id']
		course = Course.objects.get(pk=course_id)
		students = course.student_set.all()	
	else:	
		students = Student.objects.all()
	return render(request, 'list_students.html', {'students': students})

def student(request, student_id):
	student = Student.objects.get(pk=student_id)
	return render (request, 'student.html', {'student': student})	