# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse,  HttpRequest
from django.views import generic
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django import forms
from courses.models import Course
from models import Student
from pybursa.utils import detail_view
from pybursa.views import MixinCourseContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import (
    FormView,
    CreateView,
    UpdateView,
    DeleteView
)

import logging
logger = logging.getLogger(__name__)


class StudentDetailView(DetailView):
    model = Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        # template_name = "..."
        # context_object_name = "st"


class StudentListView(MixinCourseContext, ListView):
    model = Student
    context_object_name = "students"
    paginate_by = 2
    template_name = "stundets/student_detail.html"

    def get_queryset(self):
        logger.debug("Debug error in student list")
        logger.info("Info in student list")
        logger.warning("Warning  in student list")
        logger.error("Critical error in student list")
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm

    def form_valid(self, form):
        response = super(StudentCreateView, self).form_valid(form)
        messages.success(
            self.request, u'Студент %s %s успешно добавлен'
            % (self.object.name, self.object.surname)
            )
        return response

    success_url = reverse_lazy('students:students')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['page_title'] = "Создание нового студента"
        return context


class StudentUpdateView(UpdateView):
    model = Student

    def get_success_url(self):
        return reverse(
            'students:edit_student', kwargs={'pk': self.object.pk, }
            )

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = "Редактирование данных студента"
        return context

    def form_valid(self, form):
        response = super(StudentUpdateView, self).form_valid(form)
        messages.success(
            self.request, u'Данные студента %s %s успешно изменены'
            % (self.object.name, self.object.surname))
        return response


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:students')

    def delete(self, request, *args, **kwargs):
        response = super(
            StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.warning(request, u'Студент %s %s был успешно удален'
                                  % (self.object.name, self.object.surname))
        return response
