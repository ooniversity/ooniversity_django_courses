# -*- coding: utf-8 -*-

from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.contrib import messages
from students.models import Student


def student_list(request):
    course_id = request.GET.get('course_id')
    if course_id == None:
        students = Student.objects.all()
    else:
        students = Student.objects.filter(courses=course_id)
    return render(request, 'students/student_list.html',
                  {'students': students})


def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    courses = student.courses.all()
    return render(request, 'students/student_detail.html', 
                  {'student': student, 'courses': courses})


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = Student()
            new_student = form.save()
            messages.success(request, 
                             u"Студент {0} успешно добавлен"\
                              .format(new_student.full_name()))
            return redirect('students:student_list')
        else:
            return render(request, 'students/student_add.html', {'form': form})
    else:
        form = StudentForm()   
    return render(request, 'students/student_add.html', {'form': form})


def student_edit(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, 
                            u"Изменения данных студента сохранены в {0}"\
                             .format(datetime.now().strftime("%H:%M:%S")))
            return redirect('students:student_edit', student_id)
        else:
            return render(request, 
                          'students/student_edit.html', {'form': form})
    else:
        form = StudentForm(instance=student)   
    return render(request, 'students/student_edit.html', {'form': form})


def student_remove(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        full_name = student.full_name()
        student.delete()
        messages.success(request,u"Студент {0} был удалён"\
                         .format(full_name))
        return redirect('students:student_list')
    return render(request, 'students/student_remove.html', {'student': student})

