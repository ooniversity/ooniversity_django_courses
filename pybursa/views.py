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
        course_name = course_current.name
        course_description = course_current.description
        student_id = str(course_id)
        lessons = Lesson.objects.filter(course = course_current) 
        message = ""
        return render(request, 'course_detail.html', {"lessons": lessons, "message": message, "student_id": student_id, "course_name": course_name, "course_description": course_description})
    except ObjectDoesNotExist:
        message = "Sorry, no course with id = " + course_id + " exists yet."
        return render(request, 'course_detail.html', {"message": message})
#https://docs.djangoproject.com/en/1.8/ref/models/querysets/#django.db.models.query.QuerySet.get

def students(request):
    course_id = request.GET.get('course_id', '') #TO CHANGE default "" afterwards!    
    course_name = ""#in order not to be referenced before assignment 
    if course_id:
        course_name = Course.objects.get(id=int(course_id))
        course_students = Student.objects.filter(courses__id = course_id)
    else:
        course_students = Student.objects.all()
    for item in course_students:
        #student_id = item.id
        #item.url = str(student_id) + "/"
        item.url = str(item.id) + "/"
    return render(request, 'students.html',  {"course_students": course_students, "course_name": course_name})

def students_full(request):
    students_full = Student.objects.all()
    for item in students_full:
        item.name
        item.surname
        student_id = item.id
        
    return render(request, 'students_full.html',  {"students_full": students_full})

def student_one(request, student_id):
    try:
        student_one = Student.objects.get(id=int(student_id))
        msg = ""
        return render(request, 'student_one.html',  {"student_one": student_one, "msg": msg, "student_id": student_id})
    except ObjectDoesNotExist:        
        msg = "Sorry, no student with id = " + student_id + " takes our courses yet."
        return render(request, 'student_one.html',  {"msg": msg})
