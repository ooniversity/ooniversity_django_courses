from django.shortcuts import render
from students.models import Student
from courses.models import Course

def showStuds(request)
    return render(request, 'student_list.html')
