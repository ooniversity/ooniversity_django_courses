# -*- coding: utf-8 -*-

from datetime import datetime
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from students.models import Student
from students.forms import StudentForm
import logging


logger = logging.getLogger(__name__)


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

    def get_context_data(self, **kwargs):
        logger.debug('Logging is running in debug mode')
        logger.info('Before getting context data')
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        logger.warning('Context data exist!')
        logger.error('Everything is correct, but we need the error message for task 11')
        return context

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
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
    form_class = StudentForm
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

