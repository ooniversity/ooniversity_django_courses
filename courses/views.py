# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from courses.forms import CourseModelForm, LessonModelForm
from courses.models import Course


def detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/detail.html', {'course': course})


def create(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, u'Курс {} успешно создан.'.format(course.name))
            return redirect('index')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})


def edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, u'Данные изменены.')
            return redirect('courses:edit', course.id)
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form': form})


def remove(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        course.delete()
        messages.success(request, u'Курс {} был удален.'.format(course.name))
        return redirect('index')
    return render(request, 'courses/remove.html', {'course': course})


def add_lesson(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, u'Занятие {} было создано.'.format(lesson.subject))
            return redirect('courses:detail', lesson.course_id)
    else:
        form = LessonModelForm(initial={'course': course})
    return render(request, 'courses/add_lesson.html', {'form': form})
