# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from courses.models import Course
from courses.forms import CourseForm, LessonForm


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail_course.html'
    context_object_name = 'course'


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('courses:index')
    template_name = 'courses/add_course.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context_data = super(CourseCreateView, self).get_context_data(**kwargs)
        context_data['page_title'] = 'Создать курс'
        context_data['h3_title'] = 'Создание нового курса'
        context_data['cancel_url'] = reverse_lazy('courses:index')
        return context_data

    def form_valid(self, form):
        response = super(CourseCreateView, self).form_valid(form)
        messages.success(self.request, u'Курс {0} успешно добавлен'.format(self.object.name))
        return response


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('courses:index')
    template_name = 'courses/add_course.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context_data = super(CourseUpdateView, self).get_context_data(**kwargs)
        context_data['page_title'] = 'Редактирование курса'
        context_data['h3_title'] = 'Редактирование данных курса'
        context_data['cancel_url'] = 'courses:index'
        return context_data

    def form_valid(self, form):
        response = super(CourseUpdateView, self).form_valid(form)
        messages.success(self.request, u'Данные курса {0} успешно изменены'.format(self.object.name))
        return response


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:index')
    template_name = 'courses/delete_course.html'
    context_object_name = 'course'

    def delete(self, request, *args, **kwargs):
        response = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        messages.success(request, u'Курс {0} успешно удален'.format(self.object.name))
        return response


class IndexView(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'courses_list'

    def get_queryset(self):
        return Course.objects.all()


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    template_name = 'courses/detail_course.html'
    return render(request, template_name, {'course': course})


def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            new_course = form.save()
            messages.success(request, 'Курс {0} успешно добавлен'.format(new_course))
            return redirect('courses:index')
    else:
        form = CourseForm()
    template_name = 'courses/add_course.html'
    return render(request, template_name, {'form': form})


def edit_course(request, pk):
    current_course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=current_course)
        if form.is_valid():
            current_course = form.save()
            messages.success(request, 'Данные курса {0} успешно изменены'.format(current_course))
            return redirect('courses:index')
    else:
        form = CourseForm(instance=current_course)
    template_name = 'courses/edit_course.html'
    return render(request, template_name, {'form': form})


def delete_course(request, pk):
    current_course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        current_course.delete()
        messages.success(request, 'Курс {0} успешно удален'.format(current_course))
        return redirect('courses:index')
    template_name = 'courses/delete_course.html'
    return render(request, template_name, {'course': current_course})


def add_lesson(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            new_lesson = form.save()
            messages.success(request, 'Занятие {0} успешно добавлено'.format(new_lesson))
            return redirect('courses:detail', pk=pk)
    else:
        form = LessonForm(initial={'course_id': pk})
    template_name = 'courses/add_lesson.html'
    return render(request, template_name, {'course': course, 'form': form})