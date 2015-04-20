#!/user/bin/python
# -*- coding: UTF-8 -*-

from django import forms
from django.shortcuts import render, redirect
from students.models import Student
from django.contrib import messages

def students_all(request):
    if not request.GET.get('course_id'):
        students_all = Student.objects.all().order_by('surname')
        return render(request, 'students/students_all.html', {'students_all': students_all})
    else:
        course_num = request.GET.get('course_id')
        students_all = Student.objects.filter(courses=course_num).order_by('surname')
        return render(request, 'students/students_all.html', {'students_all': students_all})

def student_info(request, student_id):
    student_info = Student.objects.get(id=student_id)
    return render(request, 'students/student_info.html', {'student_info': student_info})


class StudentApplicationForm(forms.ModelForm):
    class Meta:
        model = Student


def student_add(request):
    if request.method == 'POST':
        form = StudentApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(request, u'Студент %s %s успешно добавлен' %(application.surname, application.name))
            return redirect('students:students_all')
    else:
        form = StudentApplicationForm()
    return render(request, 'students/student_add.html', {'form': form})

def student_edit(request, student_id):
    application = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentApplicationForm(request.POST, instance=application)
        if form.is_valid():
            application = form.save()
            messages.success(request, u'Данные о студенте %s %s изменены' %(application.surname, application.name))
            return redirect('students:student_edit', application.id)
    else:
        form = StudentApplicationForm(instance=application)
    return render(request, 'students/student_edit.html', {'form': form, 'application': application})

def student_remove(request, student_id):
    application = Student.objects.get(id=student_id)
    if request.method == 'POST':
        application.delete()
        messages.success(request, u'Студент %s %s удален' %(application.surname, application.name))
        return redirect('students:students_all')
    return render(request, 'students/student_remove.html', {'application': application})

