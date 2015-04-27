# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.shortcuts import render, redirect
from django.contrib import messages
from models import Student
from django import forms
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class StudentAddingForm(forms.ModelForm):

    class Meta:
        model = Student


class StudentsListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        course_id = self.request.GET.get('course_id')
        if course_id:
            students = Student.objects.filter(courses=course_id)
        else:
            students = Student.objects.all()
        return students

    def get_context_data(self, **kwargs):
        context = super(StudentsListView, self).get_context_data(**kwargs)
        course_id = self.request.GET.get('course_id')
        if course_id:
            pagination_prefix = u'?course_id={0}&'.format(course_id)
        else:
            pagination_prefix = u'?'
        context['pagination_prefix'] = pagination_prefix
        return context


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:student_list')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        form = super(StudentCreateView, self).form_valid(form)
        messages.success(self.request, 
                 u"Студент '{0}' успешно добавлен".format(self.object.full_name()))
        return form


class StudentUpdateView(UpdateView):
    model = Student
    success_url = '#'
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        form = super(StudentUpdateView, self).form_valid(form)
        messages.success(self.request, u"Изменения сохранены")
        return form


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:student_list')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        return context

    def delete(self, request, *args, **kwargs):
        response = super(StudentDeleteView, self).delete(self, request, *args, **kwargs)
        messages.success(request, u"Студент '{0}' был удалён".format(self.object.full_name()))
        return response
