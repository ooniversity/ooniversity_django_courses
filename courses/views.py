# -*- coding: utf-8 -*-
from django.views import generic
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from models import Course, Lesson
from coaches.models import Coach
from django.contrib import messages
from django import forms
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import (
    FormView,
    CreateView,
    UpdateView,
    DeleteView
)


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/courses.html"


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/add.html"

    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['page_title'] = "Создание нового студента"
        return context

    def form_valid(self, form):
        response = super(CourseCreateView, self).form_valid(form)
        messages.success(
            self.request, u'Курс %s успешно добавлен' % (self.object.name)
            )
        return response


class CourseUpdateView(UpdateView):
    model = Course
    template_name = "courses/edit.html"

    def get_success_url(self):
        return reverse(
            'courses:edit_course', kwargs={'pk': self.object.pk, }
            )

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = "Редактирование данных курса"
        return context

    def form_valid(self, form):
        response = super(CourseUpdateView, self).form_valid(form)
        messages.success(
            self.request, u'Данные курса %s изменены' % (self.object.name)
            )
        return response


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = "courses/remove.html"

    def delete(self, request, *args, **kwargs):
        response = super(
            CourseDeleteView, self).delete(request, *args, **kwargs)
        messages.warning(request, u'Курс %s был успешно удален'
                                  % (self.object.name))
        return response


def add_lesson(request, pk):
    context = dict()
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(
                            request,
                            u'Урок %s успешно создался!' % (lesson.topic))
            return redirect('courses:courses', pk=pk)
    else:
        form = LessonForm(initial={'course': pk})
    context['form'] = form
    return render(request, 'courses/add_lesson.html', context)
