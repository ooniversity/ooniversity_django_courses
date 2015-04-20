#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from django import forms

from django.shortcuts import get_object_or_404, get_list_or_404

from courses.models import Course, Lesson
from coaches.models import Coach

from static.python.get_consecutive_number import get_consecutive_number


class LessonAddForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'

    def clean_consecutive_number(self):
        data = self.cleaned_data['consecutive_number']
        consecutive_number_list = []
        for i in Lesson.objects.filter(course=self.cleaned_data['course']):
            consecutive_number_list.append(i.consecutive_number)
        if data in consecutive_number_list and data != self.instance.consecutive_number:
            raise forms.ValidationError(u"Такой номер уже задействован!")
        return data


class CourseAddForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def clean_coach(self):
        data = self.cleaned_data['coach']
        if not data:
            raise forms.ValidationError(u"Выбирете преподавателя.")
        return data

    def clean_assistant(self):
        data = self.cleaned_data['assistant']
        if not data:
            raise forms.ValidationError(u"Выбирете ассистента.")

        return data

    def clean(self):
        cleaned_data = super(CourseAddForm, self).clean()
        coach = cleaned_data.get("coach")
        assistant = cleaned_data.get("assistant")

        if coach == assistant:
            msg = u"Преподаватель и ассистент должны быть разными."
            self.add_error('coach', msg)
            self.add_error('assistant', msg)
        return cleaned_data


class CourseView(generic.ListView):
    template_name = 'courses/courses.html'
    model = Course


class CourseDetialView(generic.ListView):
    template_name = 'courses/detail.html'
    model = Course

    def get_queryset(self):
        qs = get_object_or_404(Course, pk=self.kwargs['pk'])
        return qs


def add_lesson(request, pk):
    context = dict()
    context['course_id'] = pk
    if request.method == 'POST':
        form = LessonAddForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(request, 'Registration complite!')
            return redirect('courses:detail', pk=context['course_id'])
    else:
        consecutive_number = get_consecutive_number(pk)
        course_name = get_object_or_404(Course, pk=pk).name
        theme = u'{}, лекция {}'.format(course_name, consecutive_number)
        form = LessonAddForm(initial={'course': pk, 'consecutive_number': consecutive_number, 'theme': theme})
    context['form'] = form
    return render(request, 'courses/add_lesson.html', context)


def edit_lesson(request, pk):
    application = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        form = LessonAddForm(request.POST, instance=application)
        if form.is_valid():
            application = form.save()
            messages.success(request, 'Changes have been saved!')
    else:
        form = LessonAddForm(instance=application)
    return render(request, 'courses/edit_lesson.html', {'form': form, 'application': application})


def remove_lesson(request, pk):
    application = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        application.delete()
        messages.warning(request, u'Object {} deleted!'.format(application.theme))
        return redirect('courses:detail', pk=application.course.pk)
    return render(request, 'courses/delete_lesson.html', {'application': application})


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
    application = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseAddForm(request.POST, instance=application)
        if form.is_valid():
            application = form.save()
            messages.success(request, 'Changes have been saved!')
    else:
        form = CourseAddForm(instance=application)
    return render(request, 'courses/edit_course.html', {'form': form})


def course_remove(request, pk):
    application = get_object_or_404(Course, pk=pk)
    lessons = Lesson.objects.filter(course=application)
    if request.method == 'POST':
        for lesson in lessons:
            lesson.delete()
        application.delete()
        messages.warning(request, u'Object {} deleted!'.format(application.name))
        return redirect('courses:courses')
    return render(request, 'courses/delete_course.html', {'application': application, 'lessons_count': len(lessons)})
