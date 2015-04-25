#!/usr/bin/python		
# -*- coding: UTF-8 -*-

from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from students.models import Student
from coaches.models import Coach
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class FormContextMixin(object):
    def get_context_data(self, **kwargs):
        context = super(FormContextMixin, self).get_context_data(**kwargs)
        context['form_title'] = u'Создание нового курса'
        context['button_name'] = u'Создать'
        return context


class CourseDetailView(DetailView):
    model = Course
    context_object_name = "course"
    template_name = "courses/course_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course=self.object)
        context['course_current'] = self.object
        #to show relevant list of students:
        context['course_name'] = self.object.name
        context['course_id'] = self.object.id
        return context


class CourseCreateView(SuccessMessageMixin, FormContextMixin, CreateView):
    model = Course
    template_name = "courses/course_modify.html"
    success_url = reverse_lazy("index")
    success_message = 'Info on a new course successfully added!' 


class CourseUpdateView(SuccessMessageMixin, FormContextMixin, UpdateView):
    model = Course
    template_name = "courses/course_modify.html"
    success_message = 'Info successfully changed!'
    form_title = u'Редактирование данных о курсе'
    button_name = u'Сохранить'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context.update(
            {'form_title': self.form_title, 
            'button_name': self.button_name}
            )
        return context


class CourseDeleteView(DeleteView):
    model = Course
    template_name = "courses/course_delete.html"
    success_url = reverse_lazy("index")

    def delete(self, request, *args, **kwargs):        
        response = super(CourseDeleteView, self).delete(self, request, *args, **kwargs)
        name = self.object.name
        messages.success(self.request, "Info on %s has been deleted."%(name))
        return response



class LessonModification(forms.ModelForm):
    class Meta:
        model = Lesson


def lesson_add(request, pk):
    lesson = Lesson()
    form_lesson_add = LessonModification()
    if request.method == "POST":
        form_lesson_add = LessonModification(request.POST)
        if form_lesson_add.is_valid():                
            lesson = form_lesson_add.save()
            messages.success(request, 'Info on a new lesson successfully added!');
            return redirect("courses:course", pk=pk)
    else:
        form_lesson_add = LessonModification(initial={'course': pk})
    return render(request, 'courses/lesson_add.html', {"form_lesson_add": form_lesson_add})


