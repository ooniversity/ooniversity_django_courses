from django.shortcuts import render
from students.models import Student
from courses.models import Course

def students_all(request):
	#http://127.0.0.1:8000/students/
	#http://127.0.0.1:8000/students/?course_id=1

	#print request.GET.get('course_id')
	
	cid = request.GET.get('course_id')

	if cid == None:
		students = Student.objects.all()
	else:
		#course = Course.objects.get(pk=int(cid))
		#students = course.students.all()
		students = Course.objects.get(pk=int(cid)).students.all()

	return render(request, "students.html", {'students':students})


def one_of_student(request, pk):
	#http://127.0.0.1:8000/students/1/
	student = Student.objects.get(pk=pk)
	return render(request, 'oneofstudent.html', {'student':student})


