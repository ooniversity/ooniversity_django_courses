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


def course_adding(request):
    if request.method == "POST":
        form = CourseAddingForm(request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            application = form.save()
            messages.add_message(request, messages.INFO, 'Курс ' +
                                 clean.get('title') + ' успешно добавлен'
                                 )

            return redirect('index')
    else:
        form = CourseAddingForm()
    return render(request, 'add_course.html', {'form': form})


def edit_course(request, pk):
    application = Course.objects.get(id=pk)
    if request.method == "POST":
        form = CourseAddingForm(request.POST, instance=application)
        if form.is_valid():
            application = form.save()
            messages.add_message(request, messages.INFO, "Данные изменены")

            return render(request, 'change_course.html', {'form': form})
    else:
        form = CourseAddingForm(instance=application)

    return render(request, 'change_course.html', {'form': form})


def delete_course(request, pk):
    application = Course.objects.get(id=pk)
    if request.method == "POST":

        messages.add_message(request, messages.INFO, 'Курс ' + application.title +
                             ' успешно удален'
                             )
        application.delete()

        return redirect('index')
    return render(request, 'delete_course.html')	