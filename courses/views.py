# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from coaches.models import Coach
from django import forms
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from models import Course, Lesson


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/courses.html'
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        course = context['course']
        context['coach']  = Coach.objects.get(user=course.coach.user)
        context['assistant'] = Coach.objects.get(user=course.assistant.user)
        context['lessons'] = Lesson.objects.filter(course=course)
        return context


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add_course.html'
    #context_object_name = "course"
    success_url = reverse_lazy('index')


    def form_valid(self, form):
        form = super(CourseCreateView, self).form_valid(form)
        messages.success(self.request, u"Курс {} успешно добавлен".format(self.object.name))
        return form



class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit_course.html'
    context_object_name = "course"
    #success_url = reverse_lazy('courses:courses', id)

    def form_valid(self, form):
        form = super(CourseUpdateView, self).form_valid(form)
        messages.success(self.request, u"Данные о курсе {} обновлены".format(self.object.name))
        return form

    def get_success_url(self):
        return '/courses/{}/'.format(self.kwargs['pk'])



class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/remove_course.html'

    def delete(self, request, *args, **kwargs):
        response = super(CourseDeleteView, self).delete(self, request, *args, **kwargs)
        name = self.object.name
        messages.success(request, u"Курс по {0} был удалён".format(name))
        return response



def add_lesson(request, id):
    course = Course.objects.get(pk=id)
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            new_lesson = Lesson()
            new_lesson.course = course
            new_lesson = form.save()
            messages.success(request, u"Занятие {0} успешно создано".format(new_lesson.theme))
            return redirect('courses:courses', id)
        else:
            return render(request, 'courses/add_lesson.html', {'form': form}) 

    else:
        form = LessonModelForm(initial={'course':course})

    return render(request, 'courses/add_lesson.html', {'form': form}) 












