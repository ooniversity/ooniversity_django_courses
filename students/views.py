# -*- coding: UTF8 -*-
from django.shortcuts import render
from courses.models import Course
from students.models import Student


def detail(request):
    if 'course_id' in request.GET and request.GET['course_id']:
        course_id = request.GET['course_id']
        #print course_id
        if course_id=="":
            course_id='1'
        else:
            if course_id[0]=='-':
                bb=course_id[1:]
            else:
                bb=course_id
            if bb.isdigit()==False:
                course_id='1'
        course = Course.objects.filter(id=course_id)[0]
        students = Student.objects.filter(courses=course_id)
    else:
        course = Course.objects.all()
        students = Student.objects.all()
    return render(request, 'detail.html', {'course' : course, 'students' : students})


def one_student(request, pk):
    course = Course.objects.all()
    one_student = Student.objects.filter(id=pk)[0]
    return render(request, 'student.html', {'course' : course, 'one_student' : one_student})

