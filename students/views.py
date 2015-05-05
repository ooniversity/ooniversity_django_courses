from django.shortcuts import render, render_to_response, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from students.models import Student, StudentForm
from courses.models import Course

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import logging


logger = logging.getLogger(__name__)


class StudentListView(ListView):
    model = Student
    context_object_name = "students"
    paginate_by = 2

    def get_queryset(self):
        student = super(StudentListView, self).get_queryset()
        logger.debug("Debug info - list of students")
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            student = student.filter(courses=course_id)
        return student


class StudentDetailView(DetailView):
    model = Student
    logger.info("Success view detail info about student")
    logger.debug("Debug is Ok for student")
    logger.warning("Something is wrong")
    logger.error("Couldn't show a student")


class StudentCreateView(SuccessMessageMixin, CreateView):
    model = Student
    success_url = reverse_lazy('students:students-list')
# show messages on page
    success_message = "Student: %(surname)s %(name)s was added success!"


class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = Student
    success_url = reverse_lazy('students:students-list')
    template_name_suffix = '_update_form'
    success_message = "Student: %(surname)s %(name)s was updated success!"


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:students-list')
    template_name_suffix = "_check_delete"
    success_message = "Student: %(surname)s %(name)s was deleted success!"

    def delete(self, request, *args, **kwargs):
        context = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        logger.warning("Delete student for ever")
        messages.success(self.request, self.success_message % {
            'surname': self.object.surname,
            'name': self.object.name,
        })
        return context
