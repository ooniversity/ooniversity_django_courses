# coding=utf-8
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import messages

from courses.models import Course, Lesson
from CourseForm import CourseForm


class IndexView(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.order_by('-id')


def detail(request, pk):
    course = Course.objects.get(id=pk)
    lesson_list = Lesson.objects.filter(course=pk)

    return render(request, 'courses/detail.html', {
        'course': course,
        'lesson_list': lesson_list})


def contact(request):
    return render(request, 'courses/contact.html')


def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            new_course = form.save()
            info_message = 'Курс ' + str(new_course.title) + ' успешно добавлен'
            messages.success(request, info_message)
            return redirect('courses:index')
    else:
        form = CourseForm()
    action_name = "   Создать   "

    return render(request, 'courses/add.html', {
        'form': form,
        'action_name': action_name,})


def course_edit(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            new_course = form.save()
            info_message = 'Данные изменены.'
            messages.success(request, info_message)
            return redirect('courses:edit', pk=pk)
    else:
        form = CourseForm(instance=course)
    action_name = "   Изменить   "

    return render(request, 'courses/edit.html', {
        'form': form,
        'action_name': action_name,})


def course_remove(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        info_message = 'Курс ' + str(course.title) + ' был удален.'
        course.delete()
        messages.success(request, info_message)
        return redirect('courses:index')
    form = None
    action_name = "   Удалить   "

    return render(request, 'courses/remove.html', {
        'form': form,
        'action_name': action_name,
        'course': course.title,})


