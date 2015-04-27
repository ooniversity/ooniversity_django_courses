# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from models import Student
from courses.models import Course

from django import forms
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from pybursa.utils import detail_view
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView


class StudentListView(ListView):
    model = Student
    paginate_by = 2
    #context_object_name = 'students'  # improvement

    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()   #get origin queryser Student
        if self.request.GET.get('course_id'):
            course_id = self.request.GET['course_id']
            course = Course.objects.get(pk=course_id)
            qs = course.student_set.all()
        return qs

# my old function
'''
def students_of_the_course(request):
    if request.GET.get('course_id'):
        course_id = request.GET['course_id']
        course = Course.objects.get(pk=course_id)
        students = course.student_set.all()
    else:
        students = Student.objects.all()
    return render(request, 'students_of_the_course.html', {'students': students})
'''

class StudentDetailView(DetailView):
    model = Student

#import from utils
'''
def student_info(request, student_id):
    return detail_view(request, student_id, Student)
'''

# my old function
'''
def student_info(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'student_info.html', {'student': student})
'''

# creating forms from models Student
class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        labels = {'email': 'Mail'}
        help_texts = {'email': 'Enter personal email'}
        widgets = {'courses': forms.CheckboxSelectMultiple}
        fields = '__all__'

#create universal function
'''
def add_edit_student(request, student_id=None):
    if student_id is None:
        student = None
        message = "Student successfully added"
        page_title = u'Создание нового студента'
    else:
        student = Student.objects.get(pk=student_id)
        message = "Data students was successfully changed"
        page_title = u'Редактирование данных студента'
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, message)
            return redirect('students:students_of_the_course')
    else:
        form = StudentForm(instance=student)
    return render(request, 'add_edit.html', {'form': form, 'page_title': page_title})
'''

# my old view for add student
'''
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = form.save()
            messages.success(request, "Student %s %s successfully added" % (new_student.name, new_student.surname))
            return redirect('students:students_of_the_course')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})
'''
# my old view for edit student
'''
def edit_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, "Data students %s %s was successfully changed" % (student.name, student.surname))
            return redirect('students:students_of_the_course')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})
'''

#my view for delete student
'''
def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Students %s %s was successfully deleted" % (student.name, student.surname))
        return redirect('students:students_of_the_course')
    return render(request, 'delete_student.html', {'student': student})
'''


#create CrateView, UpdateView, DeleteView views
# view for create student
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students:students_of_the_course')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['page_title'] = u'Создание нового студента'
        return context

    def form_valid(self, form):
        response = super(StudentCreateView, self).form_valid(form)
        messages.success(self.request, 'Student %s %s successfully added'
                                       % (self.object.name, self.object.surname))
        return response


# view for update student
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students:students_of_the_course')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = u'Редактирование данных студента'
        return context

    def form_valid(self, form):
        response = super(StudentUpdateView, self).form_valid(form)
        messages.success(self.request, 'Data students %s %s was successfully changed'
                                       % (self.object.name, self.object.surname))
        return response


# view for delete student
class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:students_of_the_course')

    def delete(self, request, *args, **kwargs):
        response = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.warning(request, "Students %s %s was successfully deleted"
                                  % (self.object.name, self.object.surname))
        return response