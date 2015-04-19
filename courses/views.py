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


def course_d(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/courses.html', {'course': course})


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(
                            request,
                            u'Курс %s успешно добавлен' % (course.name))
            return redirect('index')
    else:
        form = CourseForm()
    return render(request, 'courses/add.html', {'form': form})


def edit_course(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, u'Курс успешно изменен')
    else:
        form = CourseForm(instance=course)
    return render(
                request,
                'courses/edit.html',
                {'form': form, 'course': course})


def remove_course(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        course.delete()
        messages.success(
                        request,
                        u'Курс %s был успешно удален' % (course.name),
                        {'course': course})
        return redirect('index')
    form = None
    return render(
                request,
                'courses/remove.html',
                {'form': form, 'course': course})


def add_lesson(request, pk):
    context = dict()
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(
                            request,
                            u'Урок %s успешно создался!' % (lesson.topic))
            return redirect('courses:courses', pk=pk)
    else:
        form = LessonForm(initial={'course': pk})
    context['form'] = form
    return render(request, 'courses/add_lesson.html', context)
