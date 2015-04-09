#!/usr/bin/python		
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from courses.models import Course, Lesson
from students.models import Student
from django.core.exceptions import ObjectDoesNotExist
#from django.db.models.base import ObjectDoesNotExist

def index(request):
    courses = Course.objects.all()
    for item in courses:
        course_id = item.id
        item.url = "courses/"+str(course_id)
    return render(request, 'index.html', {"courses": courses})

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')

#def course_detail(request):
    #return render(request, 'course_detail.html')

def course_detail(request, course_id):
    try:
        course_current = Course.objects.get(id=int(course_id))
        student_id = str(course_id)
        lessons = Lesson.objects.filter(course = course_current) 
        message = ""
        return render(request, 'course_detail.html', {"lessons": lessons, "message": message, "student_id": student_id})
    except ObjectDoesNotExist:
        message = "Sorry, no course with id = " + course_id + " exists yet."
        return render(request, 'course_detail.html', {"message": message})
#https://docs.djangoproject.com/en/1.8/ref/models/querysets/#django.db.models.query.QuerySet.get

def students(request):
    #svar = course_detail(request, course_id, student_id)
    #stud_url = var.student_id
    students = Student.objects.all()
    #course_current = Course.objects.get(id=int(course_id))

    course_id = request.GET.get('course_id', '1') #TO CHANGE default "" afterwards!

    #name = Student.objects.get(id=course_current).name#DOESN'T WORK
    course_students = Student.objects.filter(courses__id = course_id)
    for item in course_students:
        student_id = item.id
        item.url = "students/"+str(student_id) + "/"
    return render(request, 'students.html',  {"course_students": course_students})


        
