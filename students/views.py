# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.contrib import messages
from django import forms
from courses.models import Course
from models import Student
from pybursa.utils import detail_view
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class StudentDetailView(DetailView):
    model = Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # template_name = "..."
        # context_object_name = "st"


class StudentListView(ListView):
    model = Student
    template_name = "students/students.html"
    context_object_name = "students"


def students(request):
    course_id = request.GET.get('course_id', None)
    if course_id:
        students = Student.objects.filter(courses__id=course_id)
    else:
        students = Student.objects.all()
    return render(request, 'students/students.html', {'students': students})


def student_d(request, pk):
    return detail_view(request, pk, Student)


def create_edit(request, pk=None):
    if pk is None:
        student = None
        message = u'Студент успешно добавлен'
        page_title = u'Создание нового студента'
    else:
        student = Student.objects.get(id=pk)
        message = u'Данные изменены'
        page_title = u'Редактирование студента'
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, message)
            return redirect('students:students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/add_edit.html',
                {'form': form, 'page_title': page_title})


def remove_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(
                        request, u'Студент  %s %s был успешно удален' %
                        (student.name, student.surname))
        return redirect('students: students')
    form = None
    return render(request, 'students/remove.html', {'student': student})
