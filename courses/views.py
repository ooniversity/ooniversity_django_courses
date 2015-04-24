# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from models import Course, Lessons
from coaches.models import Coach
from django import forms
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class AddLessonForm(forms.ModelForm):
	class Meta:
		model = Lessons
		fields = '__all__'


class CourseDetailView(DetailView):
	model = Course
	template_name = "course.html"
	context_object_name = "course"

	def get_context_data(self, **kwargs):
		context = super(CourseDetailView, self).get_context_data(**kwargs)
		lessons = self.object.lessons_set.all()
		context['lessons'] = lessons
		return context	
	

class LessonsCreateView(CreateView):
	model = Lessons
	template_name = "add_lesson.html"
	
	def get_context_data(self, **kwargs):
		context = super(LessonsCreateView, self).get_context_data(**kwargs)
		course = Course.objects.get(pk=self.kwargs['pk'])
		context['course'] = course
		context['page_title'] = u'Добавить новое занятие'
		context['button_value'] = u'Создать'
		return context

	def get_initial(self):
		course = self.get_context_data()['course']
		self.initial =  {'course':course}
		return self.initial		

	def get_success_url(self):
		course = self.object.course
		return reverse("courses:course_description", kwargs={'pk':course.id})		

	def form_valid(self, form):
		response = super(LessonsCreateView, self).form_valid(form)
		name = self.object.theme
		messages.info(self.request, u"Урок %s успешно добавлен" % name)
		return response	


class LessonsUpdateView(UpdateView):
	model = Lessons
	template_name = "add_lesson.html"
	
	def get_context_data(self, **kwargs):
		context = super(LessonsUpdateView, self).get_context_data(**kwargs)
		context['page_title'] = u'Редактирование занятия'
		context['button_value'] = u'Изменить'
		return context

	def get_success_url(self):
		course = self.object.course
		return reverse("courses:course_description", kwargs={'pk':course.id})
			

	def form_valid(self, form):
		response = super(LessonsUpdateView, self).form_valid(form)
		messages.info(self.request, u"Данные изменены")
		return response	


class LessonsDeleteView(DeleteView):
	model = Lessons
	template_name = "delete_lesson.html"

	def get_context_data(self, **kwargs):
		context = super(LessonsDeleteView, self).get_context_data(**kwargs)
		return context

	def get_success_url(self):
		course = self.object.course
		return reverse("courses:course_description", kwargs={'pk':course.id})
				

	def delete(self, request, *args, **kwargs):
		response = super(LessonsDeleteView, self).delete(self, request, *args, **kwargs)
		name = self.object.theme
		messages.info(self.request, u"Урок %s удален" % name)
		return response		


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