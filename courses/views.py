from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from courses.models import Course, Lesson
from students.models import Student 
from coaches.models import Coach
from datetime import datetime
from django import forms


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson


def show_course(request, id):
    course = Course.objects.get(id = int(id))
    lessons = Lesson.objects.filter(course__name = course.name)
    return render(request, 'courses/course.html', {'course': course, 'lessons': lessons})


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            application = form.save()
            msg = "Course {} was added!".format(application.name)
            messages.success(request, msg)
            return redirect('index_pybursa')
    else:
        form = CourseForm()
    return render(request, 'courses/add_course.html', {'form': form})


def edit_course(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            application = form.save()
            messages.success(request, 'Course edited!')
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/edit_course.html', {'form': form})


def delete_course(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        msg = "Course {} deleted!".format(course.name)
        course.delete()
        messages.success(request, msg)
        return redirect('index_pybursa')
    return render(request, 'courses/delete_course.html', {'name': course.name})


def add_lesson(request, id):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            application = form.save()
            msg = "Lesson {} was added!".format(application.theme)
            messages.success(request, msg)
            return redirect('courses:course', application.course.id)
    else:
        form = LessonForm(initial={'course': id})
    return render(request, 'courses/add_lesson.html', {'form': form})

