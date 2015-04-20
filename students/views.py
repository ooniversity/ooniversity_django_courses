# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from models import Student
from courses.models import Course

from django import forms
from django.contrib import messages
from pybursa.utils import detail_view


def students_of_the_course(request):
    if request.GET.get('course_id'):
        course_id = request.GET['course_id']
        course = Course.objects.get(pk=course_id)
        students = course.student_set.all()
    else:
        students = Student.objects.all()
    return render(request, 'students_of_the_course.html', {'students': students})


def student_info(request, student_id):
    return detail_view(request, student_id, Student)

# my old function
#def student_info(request, student_id):
#    student = Student.objects.get(pk=student_id)
#    return render(request, 'student_info.html', {'student': student})


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        labels = {'email': 'Mail'}
        help_texts = {'email': 'Enter personal email'}
        widgets = {'courses': forms.CheckboxSelectMultiple}
        #fields = '__all__'


#create universal function
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

# my old function
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
# my old function
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

def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Students %s %s was successfully deleted" % (student.name, student.surname))
        return redirect('students:students_of_the_course')
    return render(request, 'delete_student.html', {'student': student})


