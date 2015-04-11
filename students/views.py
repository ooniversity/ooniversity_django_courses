from django.shortcuts import render, get_object_or_404
from django.views import generic

from courses.models import Course
from models import Student

def students(request):
    if request.GET.get('course_id'):
        course_id = request.GET.get('course_id')
        course = Course.objects.filter(courses=course_id)
        students = course.student_set.all()
    else:
        students = Student.objects.all()
    return render(request, 'students/students.html', {'students': students})



def student_d(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'students/student_detail.html', {'student': student})


