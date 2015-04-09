from django.shortcuts import render_to_response
from students.models import Student
from courses.models import Course

def students(request):
    course_id = request.GET.get('course_id')
    if course_id != None:
        course = Course.objects.get(pk=int(course_id))
        students = course.student_set.all().order_by('id')
        print students
    else:
       students = Student.objects.all()
    return render_to_response('student_list.html', {'students': students})

def students_details(request, pk):
    student = Student.objects.get(pk=pk)
    courses = student.courses.all()
    return render_to_response('student_detail.html', {'student': student,
        'courses': courses,
        })