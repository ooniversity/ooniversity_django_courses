#!/user/bin/python
# -*- coding: UTF-8 -*-

from django import forms
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from students.models import Student
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView


class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset().order_by('surname')
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:students_all')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        local = {'page_header': u'Создание нового студента', 
                 'block_title': 'student_add', 'button_name': u'Создать'}
        context.update(local)
        return context

    def form_valid(self, form):
        instance = form.save()
        messages.success(self.request, u'Студент %s %s успешно добавлен' %(instance.surname, instance.name))
        return super(StudentCreateView, self).form_valid(form)



class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:students_all')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        local = {'page_header': u'Редактирование данных студента', 
                 'block_title': 'student_edit', 'button_name': u'Изменить'}
        context.update(local)
        return context

    def form_valid(self, form):
        messages.success(self.request, u'Данные о студенте %s %s изменены' 
                                            %(self.object.surname, self.object.name))
        return super(StudentUpdateView, self).form_valid(form)

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:students_all')

    def delete(self, request, *args, **kwargs):
        response = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, u'Студент %s %s успешно удален' 
                                            %(self.object.surname, self.object.name))
        return response