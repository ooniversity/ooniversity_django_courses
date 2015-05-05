# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from students.models import Student
from models import Student
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from students.forms import StudentModelForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import logging
logger = logging.getLogger(__name__) #students.views

class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs
    
    def get_context_data(self, **kwargs):
        context_data = super(StudentListView, self).get_context_data(**kwargs)
        page_path = '?'
        course_id = self.request.GET.get('course_id')
        if course_id:
            page_path = '?course_id={0}&'.format(course_id)
        context_data['page_path'] = page_path
        return context_data



class StudentDetailView(DetailView):
    model = Student
    logger.debug("DEBUG logger in course")
    logger.info("INFO logger in course")
    logger.warning("WARNING logger in course")
    logger.error("ERROR logger in course")


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:students')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['page_title'] = u"Создание нового студента"
        return context

    def form_valid(self, form):
        form = super(StudentCreateView, self).form_valid(form)
        messages.success(self.request, u"Студент {} успешно добавлен".format(self.object.full_name()))
        return form


class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:students')    

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = u"Редактирование данных студента"
        return context

    def form_valid(self, form):
        form = super(StudentUpdateView, self).form_valid(form)
        messages.success(self.request, u"Изменения данных студента {0} сохранены".format(self.object.full_name()))
        return form



class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:students')

    def delete(self, request, *args, **kwargs):
        response = super(StudentDeleteView, self).delete(self, request, *args, **kwargs)
        name = self.object.full_name()
        messages.success(request, u"Студент {0} был удалён".format(name))
        return response





















