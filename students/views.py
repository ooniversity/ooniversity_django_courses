# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
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
            #student = Student.objects.get(id=9)
            messages.success(request, 'Студент успешно добавлен', {'student':student})
            return redirect('students:students')
    else:
        form = StudentForm()
    return render(request,'students/add.html', {'form':form})

def edit_student(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)

    return render(request,'students/edit.html', {'form':form})

def remove_student(request, pk):
    student = Student.objects.get(id=pk)
    return render(request,'students/remove.html')


