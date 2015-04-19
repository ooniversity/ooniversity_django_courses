#!/usr/bin/python		
# -*- coding: UTF-8 -*-

from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from students.models import Student
from coaches.models import Coach
from django.core.exceptions import ObjectDoesNotExist
#from django.db.models.base import ObjectDoesNotExist
from django import forms
from django.contrib import messages

def index(request):
    courses = Course.objects.all()
    for item in courses:
        course_id = item.id
        item.url = "courses/%s/"%(str(course_id))
    return render(request, 'index.html', {"courses": courses})

def contact(request):
    return render(request, 'contact.html')


class CoursetModification(forms.ModelForm):
    class Meta:
        model = Course


def course_add(request):
    course = Course()
    if request.method == "POST":
        form_add = CoursetModification(request.POST)
        if form_add.is_valid():                
            course = form_add.save()
            messages.success(request, 'Info on a new course successfully added!');
            return redirect("/")
    else:
        form_add = CoursetModification()
    return render(request, 'courses/course_add.html', {"form_add": form_add})


def course_edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form_edit = CoursetModification(request.POST, instance=course)
        if form_edit.is_valid():                
            course = form_edit.save()
            messages.success(request, 'Info on a course has been modified!');
            #return redirect("/")
    else:
        form_edit = CoursetModification(instance=course)
    return render(request, 'courses/course_edit.html', {"form_edit": form_edit})


def course_delete(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        course.delete()
        messages.success(request, "Course %s has been deleted."%(course.name))
        return redirect("/")
    return render(request, 'courses/course_delete.html', {"course": course})



def student_list(request):#obsolete
    return render(request, 'obsolete/student_list.html')

def student_detail(request):#obsolete
    return render(request, 'obsolete/student_detail.html')
