# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from students.models import Student
from students.forms import StudentForm


class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        queryset = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id')
        if course_id:
            queryset = queryset.filter(course__id=int(course_id))
        return queryset


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students:index')

    def get_context_data(self, **kwargs):
        context_data = super(StudentCreateView, self).get_context_data(**kwargs)
        context_data['page_title'] = 'Создать студента'
        context_data['h3_title'] = 'Создание нового студента'
        context_data['cancel_url'] = reverse_lazy('students:index')
        return context_data

    def form_valid(self, form):
        response = super(StudentCreateView, self).form_valid(form)
        messages.success(self.request, u'Студент {0} успешно добавлен'.format(self.object.full_name()))
        return response


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students:index')

    def get_context_data(self, **kwargs):
        context_data = super(StudentUpdateView, self).get_context_data(**kwargs)
        context_data['page_title'] = 'Редактирование студента'
        context_data['h3_title'] = 'Редактирование данных студента'
        context_data['cancel_url'] = reverse_lazy('students:index')
        return context_data

    def form_valid(self, form):
        response = super(StudentUpdateView, self).form_valid(form)
        messages.success(self.request, u'Данные студента {0} успешно изменены'.format(self.object.full_name()))
        return response


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:index')

    def delete(self, request, *args, **kwargs):
        response = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(request, u'Студент {0} успешно удален'.format(self.object.full_name()))
        return response


def student(request):
    if request.GET.get('course_id'):
        course_id = int(request.GET.get('course_id'))
        students_list = Student.objects.filter(course=course_id)
    else:
        students_list = Student.objects.all()
    return render(request, 'students/index.html', {'students_list': students_list})


def student_detail(request, pk):
    current_student = get_object_or_404(Student, pk=pk)
    template_name = 'students/detail_student.html'
    return render(request, template_name, {'student': current_student})


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = form.save()
            messages.success(request, u'Студент {0} успешно добавлен'.format(new_student))
            return redirect('students:index')
    else:
        form = StudentForm()
    template_name = 'students/add_student.html'
    return render(request, template_name, {'form': form})


def edit_student(request, pk):
    current_student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=current_student)
        if form.is_valid():
            current_student = form.save()
            messages.success(request, u'Данные студента {0} успешно изменены'.format(current_student))
            return redirect('students:index')
    else:
        form = StudentForm(instance=current_student)
    template_name = 'students/edit_student.html'
    return render(request, template_name, {'form': form})


def delete_student(request, pk):
    current_student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        current_student.delete()
        messages.success(request, u'Студент {0} успешно удален'.format(current_student))
        return redirect('students:index')
    template_name = 'students/delete_student.html'
    return render(request, template_name, {'student': current_student})
