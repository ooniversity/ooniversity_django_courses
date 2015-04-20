from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from students.models import Student
from courses.models import Course, Lesson
from django.views import generic

def mainP(request):
    courses = Course.objects.all()
    lessons = Lesson.objects.all()
    context = {'courses': courses, 'lessons': lessons, 'var1': "Hello World!"}
    context['var2'] = ['a', 'b', 'c']
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def stud_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", 
                 {'students': students})

def stud_detail(request):
    return render(request, 'student_detail.html')
