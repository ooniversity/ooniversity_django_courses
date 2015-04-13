# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from students.forms import StudentModelForm
from students.models import Student


def list_view(request):
    course_id = request.GET.get('course_id', None)
    if course_id:
        students = Student.objects.filter(courses__id=course_id)
    else:
        students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})


def detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/detail.html', {'student': student})


def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, u'Студент {} {} успешно добавлен.'.format(student.name, student.surname))
            return redirect('students:list')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})


def edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, u'Данные изменены.')
            return redirect('students:edit', student.id)
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})


def remove(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, u'Студент {} {} был удален.'.format(student.name, student.surname))
        return redirect('students:list')
    return render(request, 'students/remove.html', {'student': student})