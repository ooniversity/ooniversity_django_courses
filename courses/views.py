#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from django.forms import ModelForm, ValidationError
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.shortcuts import get_object_or_404, get_list_or_404

from courses.models import Course, Lesson
from coaches.models import Coach

from static.python.get_consecutive_number import get_consecutive_number


class LessonAddForm(ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'

    def clean_consecutive_number(self):
        data = self.cleaned_data['consecutive_number']
        consecutive_number_list = []
        for i in Lesson.objects.filter(course=self.cleaned_data['course']):
            consecutive_number_list.append(i.consecutive_number)
        if data in consecutive_number_list and data != self.instance.consecutive_number:
            raise ValidationError(u"Такой номер уже задействован!")
        return data


class CourseAddForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def clean_coach(self):
        data = self.cleaned_data['coach']
        if not data:
            raise ValidationError(u"Выбирете преподавателя.")
        return data

    def clean_assistant(self):
        data = self.cleaned_data['assistant']
        if not data:
            raise ValidationError(u"Выбирете ассистента.")

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


class CourseDetialView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course_info'

class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonAddForm
    template_name = 'courses/add_lesson.html'

    def get_initial(self):
        consecutive_number = get_consecutive_number(self.kwargs['pk'])
        course_name = get_object_or_404(Course, pk=self.kwargs['pk']).name
        theme = u'{}, лекция {}'.format(course_name, consecutive_number)
        initial = {'course': self.kwargs['pk'], 'consecutive_number': consecutive_number, 'theme': theme}
        return initial

    def get_context_data(self, **kwargs):
        context = super(LessonCreateView, self).get_context_data(**kwargs)
        context['course_id'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return '/courses/{}/'.format(self.kwargs['pk'])

    def form_valid(self, form):
        response = super(LessonCreateView, self).form_valid(form)
        messages.success(self.request, 'Registration complete!')
        return response


class LessonUpdateView(UpdateView):
    model = Lesson
    form_class = LessonAddForm
    template_name = 'courses/edit_lesson.html'
    success_url = '#'
    context_object_name = 'application'

    def form_valid(self, form):
        response = super(LessonUpdateView, self).form_valid(form)
        messages.success(self.request, 'Changes have been saved!')
        return response


class LessonDeleteView(DeleteView):
    model = Lesson
    template_name = 'courses/delete_lesson.html'
    context_object_name = 'application'

    def get_success_url(self):
        course_pk = Course.objects.get(lesson=Lesson.objects.get(pk=self.kwargs['pk'])).pk
        return '/courses/{}/'.format(course_pk)

    def delete(self, request, *args, **kwargs):
        response = super(LessontDeleteView, self).delete(request, *args, **kwargs)
        messages.warning(request, u'Object {} deleted!'.format(self.object.theme))
        return response

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseAddForm
    template_name = 'courses/add_course.html'
    success_url = '/courses/'

    def form_valid(self, form):
        response = super(CourseCreateView, self).form_valid(form)
        messages.success(self.request, 'Registration complete!')
        return response

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseAddForm
    template_name = 'courses/edit_course.html'
    success_url = '#'
    context_object_name = 'application'

    def form_valid(self, form):
        response = super(CourseUpdateView, self).form_valid(form)
        messages.success(self.request, 'Changes have been saved!')
        return response


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/delete_course.html'
    context_object_name = 'application'
    success_url = '/courses/'

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        lessons = Lesson.objects.filter(course=Course.objects.get(pk=self.kwargs['pk']))
        context['lessons_count'] = len(lessons)
        return context

    def delete(self, request, *args, **kwargs):
        lessons = Lesson.objects.filter(course=Course.objects.get(pk=self.kwargs['pk']))
        for lesson in lessons:
            lesson.delete()
        response = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        messages.warning(request, u'Object {} deleted!'.format(self.object.name))
        return response
