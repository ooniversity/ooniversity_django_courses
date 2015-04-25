# -*- coding: utf-8 -*-
from django import forms
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from courses.models import Course, Lesson


class LessonAdditionForm(forms.ModelForm):
	class Meta:
		model = Lesson


class CourseAdditionForm(forms.ModelForm):
	class Meta:
		model = Course
		

def courses_main(request):
	return render(request, 'courses/courses_main.html', {'courses': Course.objects.all().order_by('id')})


def course_info(request, pk):  	
	return render (request, 'courses/course_page.html',
	{'course': Course.objects.get(id=pk),
	'lessons': Lesson.objects.filter(course__id=pk).order_by('number'),
	'coach': Course.objects.get(id=pk).coach,
	'assistant': Course.objects.get(id=pk).assistant
	})


def add_lesson(request, pk):

	if request.method == 'POST':
		form = LessonAdditionForm(request.POST)
		if form.is_valid():
			application = form.save()
			messages.success(request, u'Занятие %s успешно добавлено!' %(application.theme))
			return redirect ('courses:course_info', application.pk)
	else:
		form = LessonAdditionForm()		
		
	return render (request, 'courses/add_lesson.html', {'form': form})
	

def add_course(request):
	print request.POST, request.method

	if request.method == 'POST':
		form = CourseAdditionForm(request.POST)
		if form.is_valid():
			application = form.save()
			messages.success(request, u'Курс %s успешно добавлен!' %(application.title))
			return redirect ('courses_main')  #####
	else:
		form = CourseAdditionForm()		

	return render (request, 'courses/add_course.html', {'form': form})


def edit_course(request, pk):
	application = Course.objects.get(id=pk)

	if request.method == 'POST':
		form = CourseAdditionForm(request.POST, instance=application)
		if form.is_valid():
			application = form.save()
			messages.success(request, u'Данные о курсе %s успешно изменены!' %(application.title))
	else:
		form = CourseAdditionForm(instance = application)

	return render (request, 'courses/edit_course.html', {'form': form})


def remove_course(request, pk):
	application = Course.objects.get(id=pk)

	if request.method == 'POST':
		application.delete()
		messages.success(request, u'Данные о курсе %s успешно удалены!' %(application.title))
		return redirect ('courses_main')

	return render (request, 'courses/remove_course.html',	{'application':application})
