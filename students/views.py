# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.shortcuts import render, redirect
from django.contrib import messages
from models import Student
from django import forms


class StudentAddingForm(forms.ModelForm):

    class Meta:
        model = Student


def students_list(request):
    course_id = request.GET.get('course_id')

    if course_id:
        students = Student.objects.filter(courses=course_id)
    else:
        students = Student.objects.all()

    return render(request, 'students_list.html', {'students': students})


def student_info(request, id):
    student = Student.objects.get(id=id)
    courses = student.courses.all()
    return render(request, 'student_detail.html', {'student': student, 'courses': courses})


def student_adding(request):

    if request.method == "POST":
        form = StudentAddingForm(request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            application = form.save()
            messages.add_message(request, messages.INFO, 'Студент ' +
                                 ' '.join([clean.get('name'), clean.get('surname')]) +
                                 'успешно добавлен'
                                 )

            return redirect('students:students_list')
    else:
        form = StudentAddingForm()
    return render(request, 'add_student.html', {'form': form})


def edit_student(request, pk):
    application = Student.objects.get(id=pk)
    if request.method == "POST":
        form = StudentAddingForm(request.POST, instance=application)
        if form.is_valid():
            application = form.save()
            messages.add_message(request, messages.INFO, "Данные изменены")

            # return render_to_response('students:edit_student/pk')
            return render(request, 'change_student.html', {'form': form})
    else:
        form = StudentAddingForm(instance=application)

    return render(request, 'change_student.html', {'form': form})


def delete_student(request, pk):
    application = Student.objects.get(id=pk)
    if request.method == "POST":

        messages.add_message(request, messages.INFO, 'Студент ' +
                             ' '.join([application.name, application.surname]) +
                             ' успешно удален'
                             )
        application.delete()

        return redirect('students:students_list')
    return render(request, 'delete_student.html')
