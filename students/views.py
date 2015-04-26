# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from students.models import Student
from students.forms import StudentModelForm


class StudentListView(ListView):
    model = Student

    paginate_by = 2

    def get_queryset(self):
        course_id = self.request.GET.get('course_id')
        if course_id != None:
            student_list = Student.objects.filter(courses__id=course_id)
        else:
            student_list = Student.objects.all()
        return student_list


class StudentDetailView(DetailView):
    model = Student



# Class-based Views for forms edition student:

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:student-list')

    def form_valid(self, form):
        self.student = form.save()
        message = u'Студент - {} {} - успешно добавлен !'.format(self.student.name,
                                                                 self.student.surname)
        messages.success(self.request, message)
        return super(StudentCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['block_title'] = u'Ooniversity - New student'
        context['page_title'] = u'Добавление нового студента'
        return context


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm

    def get_success_url(self):
        return reverse_lazy('students:student-edit', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.student = form.save()
        message = u'Данные о студенте - {} {} - успешно изменены !'.format(self.student.name,
                                                                           self.student.surname)
        messages.success(self.request, message)
        return super(StudentUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['block_title'] = u'Edition Student'
        context['page_title'] = u'Редактирование данных студента - '
        return context


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:student-list')

    def delete(self, request, *args, **kwargs):
        student = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        message = u'Студент - {} {} - был успешно удален !'.format(self.object.name,
                                                                   self.object.surname)
        messages.success(self.request, message)
        return student

