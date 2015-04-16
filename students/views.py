# -*- coding: utf-8 -*-

from django.shortcuts import render
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
    student = Student.objects.get(id=student_id)
    courses = student.courses.all()
    return render(request, 'students/student_detail.html', 
                  {'student': student, 'courses': courses})


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student


def student_add(request):
    print request.method
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = Student()
            new_student = form.save()
            messages.success(request, "Студент {0} успешно добавлен".format(new_student.full_name()))
            return redirect('students:student_add')
        else:
            return render(request, 'students/student_add.html', {'form': form})
    else:
        form = StudentForm()   
    return render(request, 'students/student_add.html', {'form': form})

