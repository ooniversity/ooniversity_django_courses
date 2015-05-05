# -*- coding: utf-8 -*-
from django import forms
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404

from students.models import Student

import logging
logger = logging.getLogger(__name__) 


class StudentModelForm(forms.ModelForm):
	class Meta:
		model = Student


class StudentDetailView(DetailView):
	model = Student

	logger.debug("Student debug")
	logger.info("Student info")
	logger.warning("Student warning")
	logger.error("Student error")

class StudentListView(ListView):
	model = Student
	paginate_by = 2


	def get_queryset(self):
			course_id = self.request.GET.get('course_id',  None)

			if course_id:
				students = Student.objects.filter(courses__id=course_id)
			else:
				students = Student.objects.all()

			return students

class StudentCreateView(CreateView):
	model = Student
	form_class = StudentModelForm
	success_url = reverse_lazy('students:list') 
	
	def get_context_data (self, **kwargs):
		context = super(StudentCreateView, self).get_context_data(**kwargs)
		context['page_title'] = u"Добавление студента"
		return context

	def form_valid(self, form): 
		form.save()
		messages.success(self.request, u"Студент успешно добавлен")
		return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
	model = Student
	form_class = StudentModelForm
	success_url = reverse_lazy('students:list')

	def get_context_data (self, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(**kwargs)
		context['page_title'] = u"Изменение данных студента"
		return context

	def form_valid(self, form):  
		form.save()
		messages.success(self.request, u"Данные студента успешно изменены")###
		return super(StudentUpdateView, self).form_valid(form)###


class StudentDeleteView(DeleteView):
	model = Student
	success_url = reverse_lazy('students:list')

	def get_context_data (self, **kwargs):
		context = super(StudentDeleteView, self).get_context_data(**kwargs)
		context['page_title'] = u"Удаление студента"
		messages.success(self.request, u"Данные студента успешно удалены")
		return context
