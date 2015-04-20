# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect
from models import Course, Lessons
from coaches.models import Coach
from django import forms
from django.contrib import messages


class AddLessonForm(forms.ModelForm):
	class Meta:
		model = Lessons
		fields = '__all__'


def main(request):
	courses = Course.objects.all()
	return render(request, 'main.html', {'courses': courses})
	

def course_description(request, course_id):
	course = Course.objects.get(pk = course_id)
	lessons = course.lessons_set.all().order_by('number')
	return render(request, 'course.html', {'course': course,'lessons': lessons})


def add_lesson(request, course_id):
	if request.method == "POST":
		form = AddLessonForm(request.POST)
		if form.is_valid():
			new_lesson = form.save()
			messages.success(request, u"Занятие %s было успешно создано" % new_lesson.theme)
		return redirect('courses:course_description', course_id)
	else:
		course = Course.objects.get(pk = course_id)
		form = AddLessonForm(initial={'course':course})
	return render (request, 'add_lesson.html', {'form': form})	