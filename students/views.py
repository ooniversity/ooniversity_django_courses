# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from students.models import Student
from students.forms import StudentForm


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
            messages.success(request, 'Студент {0} успешно добавлен'.format(new_student))
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
            messages.success(request, 'Данные студента {0} успешно изменены'.format(current_student))
            return redirect('students:index')
    else:
        form = StudentForm(instance=current_student)
    template_name = 'students/edit_student.html'
    return render(request, template_name, {'form': form})


def delete_student(request, pk):
    current_student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        current_student.delete()
        messages.success(request, 'Студент {0} успешно удален'.format(current_student))
        return redirect('students:index')
    template_name = 'students/delete_student.html'
    return render(request, template_name, {'student': current_student})
