# -*- coding: utf-8 -*-

from datetime import datetime
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from students.models import Student
#from students.forms import StudentForm


class StudentsListView(ListView):
    model = Student

    def get_queryset(self):
        course_id = self.request.GET.get('course_id')
        if course_id:
            students = Student.objects.filter(courses=course_id)
        else:
            students = Student.objects.all()
        return students


class StudentDetailView(DetailView):
    model = Student

class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:student_list')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['page_title'] = u"Создание нового студента"
        return context
    
    def form_valid(self, form):
        form = super(StudentCreateView, self).form_valid(form)
        messages.success(self.request, 
                 u"Студент {0} успешно добавлен"\
                  .format(self.object.full_name()))
        return form


class StudentUpdateView(UpdateView):
    model = Student
    success_url = '#'

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = u"Редактирование данных студента"
        return context
    
    def form_valid(self, form):
        form = super(StudentUpdateView, self).form_valid(form)
        messages.success(self.request, 
                         u"Изменения данных студента сохранены в {0}"\
                          .format(datetime.now().strftime("%H:%M:%S")))
        return form


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:student_list')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['page_title'] = u"Удаление студента"
        context['page_header'] = u"Студент {0} будет удалён".format(self.object.full_name())
        return context

    def delete(self, request, *args, **kwargs):
        response = super(StudentDeleteView, self).delete(self, request, *args, **kwargs)
        name = self.object.full_name()
        messages.success(request, u"Студент {0} был удалён".format(name))
        return response

