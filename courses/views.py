# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
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

#def courses(request):
    #return render(request,'courses/courses.html')


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Course успешно добавлен')
            return redirect('courses:courses')
    else:
        form = CourseForm()
    return render(request,'courses/add.html', {'form':form})

def edit_course(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Course изменен')
            return HttpResponseRedirect('http://127.0.0.1:8000/courses/edit/%i/' % course.pk)

    else:
        form = CourseForm(instance=course)
    return render(request,'courses/edit.html', {'form':form})

def remove_course(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        messages.success(request,'Course deleted')
        course.delete()
        return redirect('/')
    form = None
    return render(request,'courses/remove.html')



def add_lesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, 'Урок успешно добавлен')
            return redirect('courses:courses course.id') #added at night
    else:
        form = LessonForm()
    return render(request,'courses/add_lesson.html', {'form':form})

def edit_lesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, 'Урок изменен')
            return redirect('courses:courses')

    return render(request,'courses/edit_lesson.html', {'form':form})

def remove_lesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    if request.method == 'POST':
        messages.success(request,'Lesson deleted')
        lesson.delete()
        return redirect('students:students')
    form = None
    return render(request,'courses/remove_lesson.html')

