from students.models import Student, CourseApplication
from courses.models import Course, Lesson
from students.forms import StudentModelForm
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render, redirect
from django import forms
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

class StudentDetailView(DetailView):
    model = Student

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Student.objects.filter(courses__id=course_id)
        else:
            students = Student.objects.all()
        return students

class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:registred')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['page_title'] = 'Student add'
        return context

class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:registred')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = 'Student edit'
        return context

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:registred')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['page_title'] = 'Student remove'
        return context

