from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from students.models import Student 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
import logging
logger = logging.getLogger(__name__)


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:student_list')

    def form_valid(self, form):
        super_valid = super(StudentCreateView, self).form_valid(form)
        msg = "Student {} {} was added!".format(self.object.name, self.object.surname)
        messages.success(self.request, msg)
        return super_valid


class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:student_list')

    def form_valid(self, form):
        msg = "Student edited!"
        messages.success(self.request, msg)
        return super(StudentUpdateView, self).form_valid(form) 


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:student_list')

    def delete(self, request, *args, **kwargs):
        delete_super = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request,
                         u'Student {} deleted.'.format(self.object.name))
        return delete_super


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        courseid = self.request.GET.get('course_id', None)
        if courseid is None:
            students = Student.objects.all()
        else:
            students = Student.objects.filter(courses__id = courseid)
        return students


class StudentDetailView(DetailView):
    model = Student
    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        student = get_object_or_404(Student, pk = self.kwargs['pk'])
        logger.debug(u'Debug info for student - {} {}'.format(student.name, student.surname))
        logger.info(u'Debug description for student - {} {}'.format(student.name, student.surname))
        logger.warning(u'Debug warning info for student - {} {}'.format(student.name, student.surname))
        logger.error(u'Debug error info for student - {} {}'.format(student.name, student.surname))
        context['student'] = student
        return context
