# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.contrib import messages
from django import forms

from courses.models import Course
from models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student


def students(request):
    course_id = request.GET.get('course_id', None)
    if course_id:
        students = Student.objects.filter(courses__id=course_id)
    else:
        students = Student.objects.all()
    return render(request, 'students/students.html', {'students': students})

def student_d(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Student %s %s was successfully added' % (student.name, student.surname))
            return redirect('students:students')
    else:
        form = StudentForm()
    return render(request,'students/add.html', {'form':form})

def edit_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'The data were successfully changed')
            return HttpResponseRedirect('http://127.0.0.1:8000/students/edit/%i/' % student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request,'students/edit.html', {'form':form})

def remove_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student %s %s was successfully deleted' %  (student.name, student.surname))
        return redirect('students:students')
    form = None
    return render(request,'students/remove.html', {'student':student})


