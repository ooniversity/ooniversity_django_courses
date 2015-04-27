# -*- coding: utf-8 -*-

from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.db.models import Max
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from courses.models import Course, Lesson
from courses.forms import CourseForm, LessonForm



class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'  #Just for Task 9.2
    context_object_name = 'course'                #Just for Task 9.2

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        course = context['course']
        context['lessons'] = Lesson.objects.filter(course=course).order_by('number')
        return context


class CourseCreateView(CreateView):
    model = Course
    template_name = 'add_edit.html'
    context_object_name = 'course'                #Just for Task 9.2
    form_class = CourseForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['page_title'] = u"Создание нового курса"
        return context
    
    def form_valid(self, form):
        form = super(CourseCreateView, self).form_valid(form)
        messages.success(self.request, 
                 u'Курс "{0}" успешно добавлен'\
                  .format(self.object.name))
        return form


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'add_edit.html'
    context_object_name = 'course'                #Just for Task 9.2
    form_class = CourseForm
    success_url = '#'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = u"Редактирование курса"
        return context
    
    def form_valid(self, form):
        form = super(CourseUpdateView, self).form_valid(form)
        messages.success(self.request, 
                         u"Изменения данных курса сохранены в {0}"\
                          .format(datetime.now().strftime("%H:%M:%S")))
        return form


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'remove.html'
    context_object_name = 'course'                #Just for Task 9.2
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['page_title'] = u"Удаление курса"
        context['page_header'] = u'Курс "{0}" будет удалён'.format(self.object.name)
        return context

    def delete(self, request, *args, **kwargs):
        response = super(CourseDeleteView, self).delete(self, request, *args, **kwargs)
        messages.success(request, u'Курс "{0}" был удалён'.format(self.object.name))
        return response


def lesson_add(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    page_title = u'Создание нового занятия для курса "{0}"'.format(course.name)
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            new_lesson = Lesson()
            new_lesson = form.save(commit=False)
            new_lesson.course = course
            new_lesson = form.save()
            messages.success(request, 
                             u'Занятие "{0}" успешно добавлено'\
                              .format(new_lesson.theme))
            return redirect('courses:course_detail', course_id=course_id)
        else:
            return render(request, 'add_edit.html', {'form': form, 'page_title':page_title})
    else:
        max_number = Lesson.objects.filter(course=course).aggregate(Max('number'))
        if not max_number.get('number__max'):
            max_number['number__max'] = 0
        new_number = max_number.get('number__max', 0) + 1
        form = LessonForm(initial={'course':course, 'number':new_number})   
    return render(request, 'add_edit.html', {'form': form, 'page_title':page_title})
