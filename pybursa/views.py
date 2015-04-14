# -*- coding: utf-8 -*-
from django.shortcuts import render
from courses.models import Course
#from pybursa import urls


def show_index(request):
    courses = Course.objects.all()
    return render(request, 'index.HTML',
                 {'courses': courses})


def show_contacts(request):
    return render(request, 'contact.HTML')
