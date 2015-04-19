# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib import messages
from django.contrib.messages import get_messages
from django.forms import *

from students.models import Student
from courses.models import Course


def students(request):
    messages = get_messages(request)
    storage = []
    for message in messages:
        storage.append(message.message)
    messages = storage
    course_id = request.GET.get('course_id')
    if course_id != None:
        course = Course.objects.get(pk=int(course_id))
        students = course.student_set.all().order_by('id')
    else:
        students = Student.objects.all()
    return render_to_response('student_list.html', {'students': students, 'messages':messages})


def students_details(request, pk):
    student = Student.objects.get(pk=pk)
    courses = student.courses.all()
    return render_to_response('student_detail.html', {'student': student,
        'courses': courses,
        })


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, u"Студент {} {} успешно добавлен!".format(
                    student.name, student.surname))
            return redirect('students:students_list')
    else:
        form = StudentForm()
    return render(request, 'add_edit.html', {'form': form,})


def student_edit(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student.update_data(**form.cleaned_data)
            student.save()
            messages.success(request, u"Данные изменены!")
            return redirect('students:student_edit', id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'add_edit.html', {'form': form,})


def student_delete(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == "POST":
        student.delete()
        messages.success(
            request, u"Студент {} {} был удалён".format(
                student.name, student.surname))
        return redirect('students:students_list')
    else:
        return render(request, 'delete.html', {'student': student,})