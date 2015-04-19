# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from students.models import Student
from django.utils.datastructures import MultiValueDictKeyError
from models import Student
from django import forms
from django.contrib import messages

def student(request):
    try:
        crs_id = int(request.GET['course_id'])
        studs = Student.objects.filter(courses=crs_id)
        print studs
        print studs[0].courses
        return render(request, 'students/students.html', {'studik': studs})
    except MultiValueDictKeyError:
        studs = Student.objects.all()
        return render(request, 'students/students.html', {'studik': studs})
    

def get_student(request, s_id):
    stu = Student.objects.get(id=s_id)	
    
    return render(request, 'students/student.html', {'st':stu})




class StudentForm(forms.ModelForm):
    class Meta:
        model = Student



def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = form.save()
            messages.success(request, u"Студент {0} {1} успешно добавлен".format(new_student.name, new_student.surname))
            return redirect('students:students')
        else:
            return render(request, 'students/add_student.html', {'form': form}) 

    else:
        form = StudentForm()

    return render(request, 'students/add_student.html', {'form': form})
    

def edit_student(request, id):
    student = Student.objects.get(pk=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, u"Данные изменены.")
            return redirect('students:edit_student', id)
        else:
            return render(request, 'students/edit_student.html', {'form': form}) 

    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit_student.html', {'form': form})


def remove_student(request, id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        student.delete()
        messages.success(request,u"Студент {0} был удалён".format(student.full_name()))
        return redirect('students:students')
    
    return render(request, 'students/remove_student.html', {'student':student})



















