# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.db.models import Max
from django.http import HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from models import Course, Lesson


class LessonAddingForm(forms.ModelForm):

    class Meta:
        model = Lesson


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        course = context['course']
        context['lessons'] = Lesson.objects.filter(course=course).order_by('num')
        return context


class CourseCreateView(CreateView):
    model = Course
    template_name = 'add_course.html'
    context_object_name = 'course'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        form = super(CourseCreateView, self).form_valid(form)
        messages.success(self.request, 
                 u'Курс "{0}" успешно добавлен'.format(self.object.title))
        return form


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'course_edit.html'
    context_object_name = 'course'
    success_url = '#'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        form = super(CourseUpdateView, self).form_valid(form)
        messages.success(self.request, u"Изменения успешно сохранены")
        return form


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'course_delete.html'
    context_object_name = 'course'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        return context

    def delete(self, request, *args, **kwargs):
        response = super(CourseDeleteView, self).delete(self, request, *args, **kwargs)
        messages.success(request, u'Курс "{0}" успешно удалён'.format(self.object.title))
        return response


def course_info(request, id):
    course = Course.objects.get(pk=id)
    lessons = Lesson.objects.filter(course=course)

    return render(request, 'courseinfo.html', {'course': course, 'lessons': lessons})


def lesson_adding(request, id):
    if request.method == "POST":
        form = LessonAddingForm(request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            application = form.save()
            messages.add_message(request, messages.INFO, 'Новое занятие "' + str(clean.get('theme')) +
                                 '" успешно добавлено' )
            return HttpResponsePermanentRedirect(reverse('courses:courseinfo', args=(id)))

    else:
        lessons = Lesson.objects.filter(course_id=id)
        maxlessonnum = lessons.aggregate(Max('num'))    # определяем максимальный номер урока на курсе
        nextNum = maxlessonnum['num__max'] + 1          # предлагаем сохранить урок под след. номером после максимального

        form = LessonAddingForm(initial={'course': id, 'num': nextNum })
    return render(request, 'add_lesson.html', {'form': form})


def course_adding(request):
    if request.method == "POST":
        form = CourseAddingForm(request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            application = form.save()
            messages.add_message(request, messages.INFO, 'Курс ' +
                                 clean.get('title') + ' успешно добавлен'
                                 )

            return redirect('index')
    else:
        form = CourseAddingForm()
    return render(request, 'add_course.html', {'form': form})


def edit_course(request, pk):
    application = Course.objects.get(id=pk)
    if request.method == "POST":
        form = CourseAddingForm(request.POST, instance=application)
        if form.is_valid():
            application = form.save()
            messages.add_message(request, messages.INFO, "Данные изменены")

            return render(request, 'change_course.html', {'form': form})
    else:
        form = CourseAddingForm(instance=application)

    return render(request, 'change_course.html', {'form': form})


def delete_course(request, pk):
    application = Course.objects.get(id=pk)
    if request.method == "POST":

        messages.add_message(request, messages.INFO, 'Курс ' + application.title +
                             ' успешно удален'
                             )
        application.delete()

        return redirect('index')
    return render(request, 'delete_course.html')
