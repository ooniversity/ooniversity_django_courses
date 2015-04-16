#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from django import forms

from courses.models import Course, Lesson
from coaches.models import Coach

from static.python.get_consecutive_number import get_consecutive_number


class LessonAddForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseAddForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def clean_assistant(self):
        data = self.cleaned_data['assistant']
        if data == self.cleaned_data['coach']:
            raise forms.ValidationError(u"Преподаватель и ассистент должны быть разными.")
        return data


class CourseView(generic.ListView):
    template_name = 'courses/courses.html'
    model = Course


class CourseDetialView(generic.ListView):
    template_name = 'courses/detail.html'
    model = Course

    def get_queryset(self):
        qs = super(CourseDetialView, self).get_queryset().filter(id=self.kwargs['id'])
        return qs


def add_lesson(request, pk):
    context = dict()
    context['course_id'] = pk
    if request.method == 'POST':
        form = LessonAddForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(request, 'Registration complite!')
            return redirect('courses:detail', id=context['course_id'])
    else:
        consecutive_number = get_consecutive_number(pk)
        course_name = Course.objects.get(pk=pk).name
        theme = u'{}, лекция {}'.format(course_name, consecutive_number)
        form = LessonAddForm(initial={'course': pk, 'consecutive_number': consecutive_number, 'theme': theme})
    context['form'] = form
    return render(request, 'courses/add_lesson.html', context)


def course_add(request):
    context = dict()
    if request.method == 'POST':
        form = CourseAddForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(request, 'Registration complite!')
            return redirect('courses:courses')
    else:
        form = CourseAddForm()
    context['form'] = form
    return render(request, 'courses/add_course.html', context)

def course_edit(request, pk):
    application = Course.objects.get(pk=pk)
    if request.method == 'POST':
        form = CourseAddForm(request.POST, instance=application)
        if form.is_valid():
            application = form.save()
            messages.success(request, 'Changes have been saved!')
    else:
        form = CourseAddForm(instance=application)
    return render(request, 'courses/edit_course.html', {'form': form})

def course_remove(request, pk):
    application = Course.objects.get(pk=pk)
    lessons = Lesson.objects.filter(course=application)
    if request.method == 'POST':
        for lesson in lessons:
            lesson.delete()
        application.delete()
        messages.warning(request, u'Object {} deleted!'.format(application.name))
        return redirect('courses:courses')
    return render(request, 'courses/delete_course.html', {'application': application})