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
    return render(request, 'index.html', {"courses": courses})

def contact(request):
    return render(request, 'contact.html')

def student_list(request):#obsolete
    return render(request, 'obsolete/student_list.html')

def student_detail(request):#obsolete
    return render(request, 'obsolete/student_detail.html')
