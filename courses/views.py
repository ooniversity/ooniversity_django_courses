# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib import messages
from django.forms import *

from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from courses.models import Course, Lesson

import logging


logger = logging.getLogger(__name__)


class CourseView(ListView):
    model = Course
    template_name = 'index.html'
    context_object_name = 'model'

class CoursePlanView(DetailView):
    model = Course
    template_name = 'courses.html'
    context_object_name = 'planmodel'

    def get_context_data(self, **kwargs):
        planmodel = super(CoursePlanView, self).get_context_data(**kwargs)
        planmodel['lessons'] = (
            self.object.coursekey.all().order_by('order_number'))
        logger.debug('courses_debug_message')
        logger.info('courses_info_message')
        logger.warning('courses_warning_message')
        logger.error('courses_error_message')
        return planmodel

class CourseCreateView(SuccessMessageMixin, CreateView):
    model = Course
    success_url = reverse_lazy('main')
    template_name = "cadd_edit.html"
    success_message = u"Курс: '%(name)s' успешно создан!"


class CourseUpdateView(SuccessMessageMixin, UpdateView):
    model = Course
    success_url = "#"
    template_name = "cadd_edit.html"
    success_message = u"Данные изменены!"


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('main')
    template_name = "cdelete.html"

    def delete(self, request, *args, **kwargs):
        response = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        messages.warning(request, u'Курс %s был удалён!' % self.object.name)
        return response

class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'


def lesson_add(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, u"Занятие %s было создано!" % lesson.subject)
            return redirect('courses:lessons', course_id)
    else:
        form = LessonForm(initial={'course': course})
    return render(request, 'ladd_edit.html', {'form': form})

def lesson_edit(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    course = lesson.course
    if request.method == "POST":
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            lesson.update_data(**form.cleaned_data)
            lesson.save()
            messages.success(request, u"Данные изменены!")
            return redirect('courses:lesson_edit', pk)
    else:
        form = LessonForm(instance=lesson)
    return render(request, 'ladd_edit.html', {'form': form, 'course': course})

def lesson_delete(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    course = lesson.course
    if request.method == "POST":
        lesson.delete()
        messages.success(request, u"Занятие %s было удалёно" % lesson.subject)
        return redirect('courses:lessons', course.id)
    else:
        return render(request, 'ldelete.html', {'lesson': lesson, 'course': course})