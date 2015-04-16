# -*- coding: UTF-8 -*-
from django.shortcuts import render,  redirect
from models import Student
from courses.models import Course
from django import forms
from django.contrib import messages


class StudentForm(forms.ModelForm):
	class Meta:
	    model = Student
	    fields = '__all__'


def list_students(request):
	if request.GET.get('course_id'):
		course_id = request.GET['course_id']
		course = Course.objects.get(pk=course_id)
		students = course.student_set.all()
	else:
		students = Student.objects.all()
	return render(request, 'list_students.html', {'students': students})


def student(request, student_id):
	student = Student.objects.get(pk=student_id)
	return render (request, 'student.html', {'student': student})


def add_student(request):
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			new_student = form.save()
			messages.success(request, u"Студент %s успешно добавлен" % new_student.fullname())
		return redirect('students:list-students')
	else:
		form = StudentForm()
	return render (request, 'add_student.html', {'form': form})	


def edit_student(request, student_id):
	student = Student.objects.get(pk=student_id)
	if request.method == "POST":
		form = StudentForm(request.POST, instance=student)
		if form.is_valid():
			student = form.save()
			messages.success(request, u"Данные изменены")
	else:
		form = StudentForm(instance=student)
	return render (request, 'edit_student.html', {'form': form})


def remove_student(request, student_id):
	student = Student.objects.get(pk=student_id)
	if request.method == "POST":
		student.delete()
		messages.success(request, u"Студент %s успешно удален" % student.fullname())
		return redirect('students:list-students')
	return render (request, 'remove_student.html', {'student':student})