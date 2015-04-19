# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from students.models import Student
from django import forms
from django.contrib import messages
from django.http import HttpResponse


class StudentAdditionForm(forms.ModelForm):
	class Meta:
		model = Student


def students_on_course(request): 
	
	if not request.GET.get('course_id'):
		students = Student.objects.all()
		return render (request, 'students/student_list.html', {'students': students})
	else:
		checked_course = request.GET.get('course_id')	
		students_on_course = Student.objects.filter(courses=checked_course).order_by('surname')
		return render (request, 'students/student_courses.html', {'students': students_on_course}) 

def student_info(request, student_id):
	return render (request, 'students/student_page.html',
	{'student_info': Student.objects.get(id=student_id),
	})

def add_student(request):
	print request.POST, request.method
	if request.method == 'POST':
		form = StudentAdditionForm(request.POST)
		if form.is_valid():
			application = form.save()
			messages.success(request, u'Студент %s %s успешно добавлен!' %(application.name, 
				             application.surname))
			return redirect ('students:students_on_course')
	else:
		form = StudentAdditionForm()		
	return render (request, 'students/add_student.html', {'form': form})

def edit_student(request, student_id):
	application = Student.objects.get(id=student_id)
	if request.method == 'POST':
		form = StudentAdditionForm(request.POST, instance=application)
		if form.is_valid():
			application = form.save()
			messages.success(request, u'Данные о студенте %s %s успешно изменены!' %(application.name, 
				             application.surname))
	else:
		form = StudentAdditionForm(instance = application)
	return render (request, 'students/edit_student.html',{'form': form})


def remove_student(request, student_id):
	application = Student.objects.get(id=student_id)
	if request.method == 'POST':
		application.delete()
		messages.success(request, u'Данные студента %s %s успешно удалены!' %(application.name, 
			             application.surname))
		return redirect ('students:students_on_course')
	return render (request, 'students/remove_student.html',	{'application':application})
