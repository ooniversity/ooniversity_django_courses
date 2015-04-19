# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Course, Lesson
from django import forms
from django.contrib import messages

class LessonAdditionForm(forms.ModelForm):
	class Meta:
		model = Lesson


def courses_main(request):
	return render(request, 'courses/courses_main.html', {'courses': Course.objects.all().order_by('id')})	

def course_info(request, course_id):  	
	return render (request, 'courses/course_page.html',
	{'course': Course.objects.get(id=course_id),
	'lessons': Lesson.objects.filter(course__id=course_id).order_by('number'),
	'coach': Course.objects.get(id=course_id).coach,
	'assistant': Course.objects.get(id=course_id).assistant
	})

def add_lesson(request, course_id):
	if request.method == 'POST':
		form = LessonAdditionForm(request.POST)
		if form.is_valid():
			application = form.save()
			messages.success(request, u'Занятие %s успешно добавлено!' %(application.theme))
			return redirect ('courses:course_info', application.course_id)
	else:
		form = LessonAdditionForm()		
	return render (request, 'courses/add_lesson.html', {'form': form})


