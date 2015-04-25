#!/usr/bin/python
# -*- coding: UTF-8 -*-


from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.forms import ModelForm, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget

from django.shortcuts import get_object_or_404

from static.python.AdminImageWidget import AdminImageWidget
from students.models import Student
from courses.models import Course


birth_years = xrange(2015, 1930, -1)


class StudentAddForm(ModelForm):

    class Meta:
        model = Student
        widgets = {
            'course': CheckboxSelectMultiple(),
            'date_of_birth': SelectDateWidget(years=birth_years),
            'image': AdminImageWidget()
            }
        labels = {'image': 'Photo'}
        help_texts = {
            'course': "You can choose more then one course.",
            'image': 'Not a required field.',
            'address': 'Not a required field.'
            }
        fields = '__all__'


class StudentsView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        query = Course.objects.filter(pk=self.request.GET.get('course_id'))
        if query:
            return Student.objects.filter(course=query)
        else:
            return Student.objects.all()

    def get_context_data(self, **kwargs):
        context = super(StudentsView, self).get_context_data(**kwargs)
        context['course_id'] = self.request.GET.get('course_id')
        return context


class StudentView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentAddForm
    success_url = reverse_lazy('students')

    def form_valid(self, form):
        response = super(StudentCreateView, self).form_valid(form)
        messages.success(self.request, 'Registration complete!')
        return response


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentAddForm
    success_url = '#'

    def form_valid(self, form):
        response = super(StudentUpdateView, self).form_valid(form)
        messages.success(self.request, 'Changes have been saved!')
        return response


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students')

    def delete(self, request, *args, **kwargs):
        response = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.warning(request, u'Object {} {} deleted!'.format(self.object.surname, self.object.name))
        return response
