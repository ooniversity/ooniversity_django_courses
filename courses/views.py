# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.contrib import messages

from courses.models import Course
from courses.forms import CourseForm


class IndexView(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'courses_list'

    def get_queryset(self):
        return Course.objects.all()


def course_detail(request, course_id):
    c = get_object_or_404(Course, pk=course_id)
    course_lesson_list = c.lesson_set.all()
    template_name = 'courses/detail_course.html'
    return render(request, template_name, {'course': c,
                                           'course_lesson_list': course_lesson_list,
                                           })


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
