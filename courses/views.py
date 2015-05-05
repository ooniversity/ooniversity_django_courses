# -*- coding: UTF-8 -*-

from django import forms
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import Course, Lesson
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

import logging

logger = logging.getLogger(__name__)


class CourseListView(ListView):
    model = Course
    template_name ='courses/main.html'
    context_object_name = 'courses_list'
    queryset = Course.objects.all().order_by('id')


class CourseDetailView(DetailView):
    model = Course
    template_name ='courses/course_info.html'
    context_object_name = 'current_course'
    logger.debug('DEBUG in courses detail!!')
    logger.info('INFO in courses detail!!')
    logger.warning('WARNING in courses detail!')
    logger.error(u'Ошибка произошла в детальном описании курса!')


class CourseCreateView(CreateView):
    model = Course
    template_name ='courses/course_add.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        instance = form.save()
        messages.success(self.request, u'Курс %s успешно добавлен' 
                                            %(instance.name))
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    template_name ='courses/course_edit.html'

    def form_valid(self, form):
        messages.success(self.request, u'Данные о курсе %s изменены' 
                                            %(self.object.name))
        return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    template_name ='courses/course_remove.html'
    context_object_name = 'application'
    success_url = reverse_lazy('main')

    def delete(self, request, *args, **kwargs):
        response = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, u'Курс %s успешно удален' 
                                            %(self.object.name))
        return response


class LessonApplicationForm(forms.ModelForm):
    class Meta:
        model = Lesson

def add_lesson(request, course_id):
    if request.method == 'POST':
        form = LessonApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(request, u'Занятие %s было создано' %(application.topic))
            return redirect('courses:course_info', application.course_id)
    else:
        form = LessonApplicationForm(initial={'course': course_id})
    return render(request, 'courses/add_lesson.html', {'form': form})

