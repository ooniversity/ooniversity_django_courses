# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from models import Course, Lesson
from coaches.models import Coach
from django.contrib import messages
from django import forms

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course

def course_d(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/courses.html', {'course':course})


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, "Course %s was successfully added" % (course.name))
            return redirect('index')
    else:
        form = CourseForm()
    return render(request,'courses/add.html', {'form':form})

def edit_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, "The data were successfully changed")
            return HttpResponseRedirect('http://127.0.0.1:8000/courses/edit/%i/' % course.id)

    else:
        form = CourseForm(instance=course)
    return render(request,'courses/edit.html', {'form':form})

def remove_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        course.delete()
        messages.success(request,"Course %s was successfully deleted" % (course.name))
        return redirect('index')
    form = None
    return render(request,'courses/remove.html', {'course':course})



def add_lesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, "Lesson %s successfully added" % (lesson.topic))
            return redirect('courses:course_d course.id') #added at night
    else:
        form = LessonForm()
    return render(request,'courses/add_lesson.html', {'form':form})



