from django.shortcuts import render
from students.models import Student


def students_on_course(request): 
	
	if not request.GET.get('course_id'):
		students = Student.objects.all()
		return render (request, 'students/student_list.html', {'students': students})
	else:
		checked_course = request.GET.get('course_id')	
		students_on_course = Student.objects.filter(courses=checked_course).order_by('surname')
		return render (request, 'students/student_courses.html', {'students': students_on_course}) 

def student_info(request, student_id):
	return render (request, 'students/student_page.html',
	{'student_info': Student.objects.get(id=student_id),
	})
