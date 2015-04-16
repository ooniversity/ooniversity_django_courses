from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from courses.models import Course, Lesson
from students.models import Student 
from coaches.models import Coach
from datetime import datetime
from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            application = form.save()
            msg = "Student {} {} was added!".format(application.name, application.surname)
            messages.success(request, msg)
            return redirect('students:student_list')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})


def edit_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            application = form.save()
            messages.success(request, 'Student edited!')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit_student.html', {'form': form})


def delete_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        msg = "Student {} {} deleted!".format(student.name, student.surname)
        student.delete()
        messages.success(request, msg)
        return redirect('students:student_list')
    return render(request, 'students/delete_student.html', {'name': student.name, 'surname': student.surname})


def show_students(request):
    if request.GET.get('course_id') is None:
        students = Student.objects.all()
        return render(request, 'students/student_list.html', {'students': students})
    else:
        students = Student.objects.filter(courses__id = int(request.GET.get('course_id')))
        return render(request, 'students/student_list.html', {'students': students})


def show_student(request, id):
    student = Student.objects.get(id = int(id))
    return render(request, 'students/student_detail.html', {'student': student})


