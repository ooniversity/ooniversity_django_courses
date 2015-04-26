# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from students.models import Student
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from students.forms import StudentForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger





class StudentListView(ListView):
    model = Student
    template_name = 'students/students.html'
    context_object_name = "students"
    paginate_by = 2
    

   
class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_info.html'
    context_object_name = "student"


class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/add_student.html'
    success_url = reverse_lazy('students:student-list')
    
    def form_valid(self, form):
        form.save()
        student_mess = 'Студент добавлен !'
        messages.success(self.request, student_mess)
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/edit_student.html'
    success_url = reverse_lazy('students:student-list')
    
    def form_valid(self, form):
        form.save()
        student_mess = 'Данные студента изменены !'
        messages.success(self.request, student_mess)
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/delete_student.html'
    success_url = reverse_lazy('students:student-list')

