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



class CourseView(ListView):
    model = Course
    template_name = 'index.html'


class CoursePlanView(DetailView):
    model = Course
    template_name = 'courses.html'
    context_object_name = 'planmodel'



class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('main')
    template_name = "cdelete.html"
    success_message = "Course: '%(title)s' was deleted success!"

    def delete(self, request, *args, **kwargs):
        context = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, self.success_message % {
            'title': self.object.title,
        })
        return context


class CourseCreateView(SuccessMessageMixin, CreateView):
    model = Course
    success_url = reverse_lazy('main')
    template_name = "cadd_edit.html"
    success_message = "Course: '%(title)s' was added success!"


class CourseUpdateView(SuccessMessageMixin, UpdateView):
    model = Course
    success_url = reverse_lazy('main')
    template_name = "cadd_edit.html"
    success_message = "Course: '%(title)s' was updated success!"


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