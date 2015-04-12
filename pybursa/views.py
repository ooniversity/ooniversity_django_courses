#!/usr/bin/python		
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from courses.models import Course, Lesson
from students.models import Student
from coaches.models import Coach
from django.core.exceptions import ObjectDoesNotExist
#from django.db.models.base import ObjectDoesNotExist

def index(request):
    courses = Course.objects.all()
    for item in courses:
        course_id = item.id
        item.url = "courses/"+str(course_id)+"/"
    return render(request, 'index.html', {"courses": courses})

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')

def coach_detail(request, co_id):
#def coach_detail(request):
    coaches = Coach.objects.get(id=int(co_id))

    coaches_info = {
        "fullname": coaches.user.get_full_name(),
        "date": coaches.birth_date,
        "address": coaches.address,
        "scype": coaches.scype,
        "phone": coaches.phone,
        #"email": coaches.user.get_email(),
        "courses_trainer": coaches.rel_trainers.all(),
        "courses_assistant": coaches.rel_assistants.all(),
        }

    
    #coaches = Coach.objects.all()
    return render(request, 'coach.html', {"coaches": coaches, "coaches_info": coaches_info})

def course_detail(request, course_id):
    try:
        course_current = Course.objects.get(id=int(course_id))
        course_name = course_current.name
        course_description = course_current.description
        student_id = str(course_id)
        lessons = Lesson.objects.filter(course = course_current)

        trainer_info = {
            "id": course_current.trainer.id,       
            "fullname": course_current.trainer.user.get_full_name(),
            "description": course_current.trainer.description,
            #"url": "coaches/"+str(course_current.trainer.id)+"/"
        }

        assistant_info = {
            "id": course_current.assistant.id,       
            "fullname": course_current.assistant.user.get_full_name(),
            "description": course_current.assistant.description,
            #"url": "coaches/"+str(course_current.assistant.id)+"/"
        }
 
        message = ""
        return render(request, 'course_detail.html', {"lessons": lessons, "message": message, "student_id": student_id, "course_name": course_name, "course_description": course_description, 'trainer_info': trainer_info, 'assistant_info': assistant_info})
    except ObjectDoesNotExist:
        message = "Sorry, no course with id = %s exists yet."%(course_id)
        return render(request, 'course_detail.html', {"message": message})
#https://docs.djangoproject.com/en/1.8/ref/models/querysets/#django.db.models.query.QuerySet.get


def students(request):
    try:
        course_id = request.GET.get('course_id', '')
        comment, course_name, course_students = "", "", "" #in order not to be referenced before assignment
        if course_id:
            course_name = Course.objects.get(id=int(course_id))
            course_students = Student.objects.filter(courses__id = course_id)
        else:
            course_students = Student.objects.all()
        for item in course_students:
            item.url = str(item.id) + "/"
        return render(request, 'students.html',  {"course_students": course_students, "course_name": course_name, "course_id": course_id})
    except ObjectDoesNotExist:
        comment = "Sorry, no course with id = %s exists yet. So no relevant students list exists."%(course_id)
        return render(request, 'students.html',  {"comment": comment})        


def student_one(request, student_id):
    try:
        student_one = Student.objects.get(id=int(student_id))
        msg = ""
        return render(request, 'student_one.html',  {"student_one": student_one, "msg": msg, "student_id": student_id})
    except ObjectDoesNotExist:        
        msg = "Sorry, no student with id = %s takes our courses yet."%(student_id)
        return render(request, 'student_one.html',  {"msg": msg})


