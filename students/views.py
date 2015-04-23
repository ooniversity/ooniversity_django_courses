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
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

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


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy("students:students")

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        #student = form.save()
        form.save()
        #messages.success(self.request, message);
        messages.success(self.request, 'Info on a new student successfully added!');
        return super(StudentCreateView, self).form_valid(form)


class StudentModification(forms.ModelForm):
    class Meta:
        model = Student


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

