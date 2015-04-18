#!/usr/bin/python		
# -*- coding: UTF-8 -*-

from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from students.models import Student
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.contrib import messages

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
        return render(request, 'students/students.html',  {"course_students": course_students, "course_name": course_name, "course_id": course_id})
    except ObjectDoesNotExist:
        comment = "Sorry, no course with id = %s exists yet. So no relevant students list exists."%(course_id)
        return render(request, 'students/students.html',  {"comment": comment})        

class StudentAddNew(forms.ModelForm):
    class Meta:
        model = Student


def student_add(request):
    student = Student()#??????????????
    if request.method == "POST":
        model_form = StudentAddNew(request.POST)
        if model_form.is_valid():                
            student = model_form.save()
            messages.success(request, 'Info on a new student successfully added!');
            return redirect("students")
    else:
        model_form = StudentAddNew()
    return render(request, 'students/student_add.html', {"model_form": model_form})


def student_one(request, student_id):
    try:
        student_one = Student.objects.get(id=int(student_id))
        msg = ""
        return render(request, 'students/student_one.html',  {"student_one": student_one, "msg": msg, "student_id": student_id})
    except ObjectDoesNotExist:        
        msg = "Sorry, no student with id = %s takes our courses yet."%(student_id)
        return render(request, 'students/student_one.html',  {"msg": msg})
