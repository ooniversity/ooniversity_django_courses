#!/usr/bin/python		
# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from students.models import Student
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
        context['form_title'] = u'Создание нового студента'
        context['button_name'] = u'Создать'
        return context


class StudentListView(ListView):
    model = Student
    #template_name = "students/students.html"
    context_object_name = "students"

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            context['course_name'] = Course.objects.get(id=course_id).name
        return context

    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id = course_id)
        return qs


class StudentDetailView(DetailView):
    model = Student
    #context_object_name = "student_one"


class StudentCreateView(SuccessMessageMixin, FormContextMixin, CreateView):
    model = Student
    success_url = reverse_lazy("students:students")
    success_message = 'Info on a new student successfully added!'
 
    """ 
    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['form_title'] = u'Создание нового студента'
        context['button_name'] = u'Создать'
        return context
    """   

    """
    def form_valid(self, form):
        #student = form.save()
        form.save()
        #messages.success(self.request, message);
        messages.success(self.request, 'Info on a new student successfully added!');
        return super(StudentCreateView, self).form_valid(form)
    """

class StudentUpdateView(SuccessMessageMixin, FormContextMixin, UpdateView):
    model = Student
    #success_url = reverse_lazy("students:students") #need to redirect to itself! if class: self.object; ассоциация урла: из словаря брать айди - %s (см.документацию); можно исползовать слаг
    success_message = 'Info successfully changed!'
    form_title = u'Редактирование данных о студенте'
    button_name = u'Сохранить'

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context.update({'form_title': self.form_title, 'button_name': self.button_name})
        return context
#http://stackoverflow.com/questions/18232851/django-passing-variables-to-templates-from-class-based-views

    """
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['form_title'] = u'Редактирование данных о студенте'
        context['button_name'] = u'Сохранить'
        return context
    """

    """
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Info successfully changed!');
        return super(StudentUpdateView, self).form_valid(form)
    """

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy("students:students")
    success_message = "Info on a student has been deleted."
    #success_message = "Info on student %s has been deleted."%(student.name)
    """    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)
    """
    def delete(self, request, *args, **kwargs):        
        response = super(StudentDeleteView, self).delete(self, request, *args, **kwargs)
        name = self.object.name
        surname = self.object.surname
        messages.success(self.request, "Info on student %s %s has been deleted."%(name, surname))
        return response    

    """
    def form_valid(self, form):
        #student = Student.objects.get(id=pk)
        #messages.success(self.request, "Info on student %s %s has been deleted."%(student.name, student.surname));
        messages.success(self.request, "Info on student has been deleted.");
        return super(StudentDeleteView, self).form_valid(form)
    """  
