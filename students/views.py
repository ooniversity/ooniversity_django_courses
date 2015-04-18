from django.shortcuts import render, get_object_or_404
from django.views import generic

from courses.models import Course
from models import Student

def students(request):
    course_id = request.GET.get('course_id', None)
    if course_id:
        students = Student.objects.filter(courses__id=course_id)
    else:
        students = Student.objects.all()
    return render(request, 'students/students.html', {'students': students})

def student_d(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

def add_stundent(request):
    return render(request,'students/add.html')
