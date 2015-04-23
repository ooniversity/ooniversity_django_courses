# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib import messages
from django.contrib.messages import get_messages
from django.forms import *

from students.models import Student
from courses.models import Course

from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class StudentsList(ListView):
    model = Student

    def get_queryset(self):
        student = super(StudentsList, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            student = student.filter(courses=course_id).order_by('id')
        return student


class StudentDetails(DetailView):
    model = Student


class StudentAdd(SuccessMessageMixin, CreateView):
    model = Student
    success_url = reverse_lazy('students:students_list')
    success_message = u"Студент %(name)s %(surname)s успешно добавлен!"


class StudentUpdate(SuccessMessageMixin, UpdateView):
    model = Student
    success_url = "#"
    template_name_suffix = '_update_form'
    success_message = u"Данные изменены !"


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('students:students_list')

    def delete(self, request, *args, **kwargs):
        response = super(StudentDelete, self).delete(request, *args, **kwargs)
        messages.warning(request, u'Cтудент {} {} был удалён!'.format(self.object.surname, self.object.name))
        return response