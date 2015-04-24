# -*- coding: UTF-8 -*-
from django.shortcuts import render,  redirect
from django.core.urlresolvers import reverse_lazy
from models import Student
from courses.models import Course
from django import forms
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class StudentForm(forms.ModelForm):
	class Meta:
	    model = Student
	    fields = '__all__'


class StudentListView(ListView):
	model = Student
	paginate_by = 2
	
	def get_queryset(self):
		course_id = self.request.GET.get('course_id' or None)
		if course_id:
			course = Course.objects.get(pk=course_id)
			student_list = course.student_set.all()
		else:
			student_list = Student.objects.all()
		return student_list

	def get_context_data(self, **kwargs):
		context = super(StudentListView, self).get_context_data(**kwargs)
		course_id = self.request.GET.get('course_id' or None)
		if course_id:
			context['course_id'] = course_id
		return context	


class StudentDetailView(DetailView):
	model = Student


class StudentCreateView(CreateView):
	model = Student
	success_url = reverse_lazy('students:list-students')

	def get_context_data(self, **kwargs):
		context = super(StudentCreateView, self).get_context_data(**kwargs)
		context['page_title'] = u'Создание нового студента'
		context['button_value'] = u'Создать'
		return context

	def form_valid(self, form):
		response = super(StudentCreateView, self).form_valid(form)
		name = self.object.fullname()
		messages.info(self.request, u"Студент %s успешно добавлен" % name)
		return response


class StudentUpdateView(UpdateView):
	model = Student
	success_url = "#"

	def get_context_data(self, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(**kwargs)
		context['page_title'] = u'Редактирование студента'
		context['button_value'] = u'Изменить'
		return context

	def form_valid(self, form):
		response = super(StudentUpdateView, self).form_valid(form)
		messages.info(self.request, u"Данные изменены")
		return response	


class StudentDeleteView(DeleteView):
	model = Student
	success_url = reverse_lazy('students:list-students')

	def get_context_data(self, **kwargs):
		context = super(StudentDeleteView, self).get_context_data(**kwargs)
		return context

	def delete(self, request, *args, **kwargs):
		response = super(StudentDeleteView, self).delete(self, request, *args, **kwargs)
		name = self.object.fullname()
		messages.info(self.request, u"Студент %s был удален" % name)
		return response


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