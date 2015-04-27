# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.contrib import admin
from courses.models import Course
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages


class CourseAddingForm(forms.ModelForm):

    class Meta:
        model = Course


def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})


def contact(request):
    return render(request, 'contact.html')
	