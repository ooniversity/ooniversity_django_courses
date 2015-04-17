# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from courses.forms import LessonModelForm
from courses.models import Course


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        super_valid = super(CourseCreateView, self).form_valid(form)
        messages.success(self.request,
                         u'Курс {} успешно создан..'.format(self.object.name))
        return super_valid


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    success_url = '/courses/edit/%(id)d/'

    def form_valid(self, form):
        messages.success(self.request, u'Данные изменены.')
        return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')

    def delete(self, request, *args, **kwargs):
        delete_super = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request,
                         u'Курс {} был удален.'.format(self.object.name))
        return delete_super


def add_lesson(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, u'Занятие {} было создано.'.format(lesson.subject))
            return redirect('courses:detail', lesson.course_id)
    else:
        form = LessonModelForm(initial={'course': course})
    return render(request, 'courses/add_lesson.html', {'form': form})
