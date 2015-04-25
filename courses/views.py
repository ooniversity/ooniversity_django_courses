# -*- coding: utf-8 -*-
from django import forms
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect

from courses.models import Course, Lesson


class LessonAdditionForm(forms.ModelForm):
	class Meta:
		model = Lesson


class CourseAdditionForm(forms.ModelForm):
	class Meta:
		model = Course
		

class CourseDetailView(DetailView):
	model = Course	
	template_name = 'courses/course_page.html'
	context_object_name = 'course'


class CourseCreateView(CreateView):
	model = Course
	form_class = CourseAdditionForm
	success_url = reverse_lazy('courses_main') 
	template_name = 'courses/add_course.html'
	
	def get_context_data (self, **kwargs):
		context = super(CourseCreateView, self).get_context_data(**kwargs)
		context['page_title'] = u"Добавление курса"
		return context

	def form_valid(self, form): 
		form.save()
		messages.success(self.request, u"Курс успешно добавлен")
		return super(CourseCreateView, self).form_valid(form)
	

class CourseUpdateView(UpdateView):
	model = Course
	form_class = CourseAdditionForm
	success_url = reverse_lazy('courses_main')
	template_name = 'courses/edit_course.html'

	def get_context_data (self, **kwargs):
		context = super(CourseUpdateView, self).get_context_data(**kwargs)
		context['page_title'] = u"Изменение данных курса"
		return context

	def form_valid(self, form):  
		form.save()
		messages.success(self.request, u"Данные курса успешно изменены")###
		return super(CourseUpdateView, self).form_valid(form)###


class CourseDeleteView(DeleteView):
	model = Course
	success_url = reverse_lazy('courses_main')
	template_name = 'courses/remove_course.html'

	def get_context_data (self, **kwargs):
		context = super(CourseDeleteView, self).get_context_data(**kwargs)
		context['page_title'] = u"Удаление курса"
		messages.success(self.request, u"Курс успешно удален")
		return context


def courses_main(request):
	return render(request, 'courses/courses_main.html', {'courses': Course.objects.all().order_by('id')})


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

