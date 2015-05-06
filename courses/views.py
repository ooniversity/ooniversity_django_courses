# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from courses.models import Course
from courses.forms import CourseForm, LessonForm

import logging
logger = logging.getLogger(__name__)


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail_course.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        logger.debug("Show DetailView courses debug")
        logger.info("Show DetailView courses info")
        logger.error("Show DetailView courses error")
        logger.warning("Show DetailView courses warning")
        return super(CourseDetailView, self).get_context_data(**kwargs)


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('courses:index')
    template_name = 'courses/add_course.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        logger.debug("show CreateView by courses ")
        context_data = super(CourseCreateView, self).get_context_data(**kwargs)
        context_data['page_title'] = 'Создать курс'
        context_data['h3_title'] = 'Создание нового курса'
        context_data['cancel_url'] = reverse_lazy('courses:index')
        return context_data

    def form_valid(self, form):
        logger.info("Form create courses success")
        response = super(CourseCreateView, self).form_valid(form)
        messages.success(self.request, u'Курс {0} успешно добавлен'.format(self.object.name))
        return response

    def form_invalid(self, form):
        response = super(CourseCreateView, self).form_valid(form)
        logger.error("Form create courses invalid!")
        return response


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('courses:index')
    template_name = 'courses/add_course.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        logger.debug("show UpdateView by courses ")
        context_data = super(CourseUpdateView, self).get_context_data(**kwargs)
        context_data['page_title'] = 'Редактирование курса'
        context_data['h3_title'] = 'Редактирование данных курса'
        context_data['cancel_url'] = 'courses:index'
        return context_data

    def form_valid(self, form):
        logger.info("Form update courses success")
        response = super(CourseUpdateView, self).form_valid(form)
        messages.success(self.request, u'Данные курса {0} успешно изменены'.format(self.object.name))
        return response


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:index')
    template_name = 'courses/delete_course.html'
    context_object_name = 'course'

    def delete(self, request, *args, **kwargs):
        logger.warning("Delete course!")
        response = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        messages.success(request, u'Курс {0} успешно удален'.format(self.object.name))
        return response


class IndexView(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'courses_list'

    def get_queryset(self):
        logger.debug("show IndexView by courses ")
        return Course.objects.all()


def add_lesson(request, pk):
    logger.debug("show form, where add lesson to course")
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            new_lesson = form.save()
            logger.info("Create lesson {0} in {1} course success".format(new_lesson, course.name))
            messages.success(request, 'Занятие {0} успешно добавлено'.format(new_lesson))
            return redirect('courses:detail', pk=pk)
    else:
        form = LessonForm(initial={'course_id': pk})
    template_name = 'courses/add_lesson.html'
    return render(request, template_name, {'course': course, 'form': form})