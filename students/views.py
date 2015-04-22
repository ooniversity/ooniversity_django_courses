#!/usr/bin/python		
# -*- coding: UTF-8 -*-

from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from students.models import Student
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class StudentListView(ListView):
    model = Student
    #template_name = "students/students.html"
    context_object_name = "students"

    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id = course_id)
        return qs



class StudentDetailView(DetailView):
    model = Student
    #context_object_name = "student_one"



def students(request):#obsolete
    try:
        course_id = request.GET.get('course_id', '')
        comment, course_name, course_students = "", "", "" #in order not to be referenced before assignment
        if course_id:
            course_name = Course.objects.get(id=course_id)
            course_students = Student.objects.filter(courses__id = course_id)
        else:
            course_students = Student.objects.all()
        return render(request, 'students/students.html',  {"course_students": course_students, "course_name": course_name, "course_id": course_id})
    except ObjectDoesNotExist:
        comment = "Sorry, no course with id = %s exists yet. So no relevant students list exists."%(course_id)
        return render(request, 'students/students.html',  {"comment": comment}) 



def student_one(request, student_id): #obsolete
    try:
        student_one = Student.objects.get(id=student_id)
        msg = ""
        return render(request, 'students/student_one.html',  {"student_one": student_one, "msg": msg, "student_id": student_id})
    except ObjectDoesNotExist:        
        msg = "Sorry, no student with id = %s takes our courses yet."%(student_id)
        return render(request, 'students/student_one.html',  {"msg": msg})


class StudentModification(forms.ModelForm):
    class Meta:
        model = Student


def student_add(request):
    #student = Student()#no need!!!
    if request.method == "POST":
        form_add = StudentModification(request.POST)
        if form_add.is_valid():                
            student = form_add.save()
            messages.success(request, 'Info on a new student successfully added!');
            return redirect("students:students")
    else:
        form_add = StudentModification()
    return render(request, 'students/student_add.html', {"form_add": form_add})


def student_edit(request, stud_id):
    student = Student.objects.get(id=stud_id)
    if request.method == "POST":
        form_edit = StudentModification(request.POST, instance=student)
        if form_edit.is_valid():                
            student = form_edit.save()
            messages.success(request, 'Info successfully changed!')
            return redirect("students:student_edit", student.id)#need to redirect! if class: self.object; ассоциация урла: из словаря брать айди - %s (см.документацию); исползовать слаг
    else:
        form_edit = StudentModification(instance=student)
    return render(request, 'students/student_edit.html', {"form_edit": form_edit})


def student_delete(request, stud_id):
    student = Student.objects.get(id=stud_id)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Info on student %s %s has been deleted."%(student.name, student.surname))
        return redirect("students:students")
    return render(request, 'students/student_delete.html', {"student": student})

