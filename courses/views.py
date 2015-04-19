# -*- coding: utf_8 -*-
from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.contrib import messages
from courses.models import Courses, Lesson


class CoursesForm(ModelForm):
    class Meta:
        model = Courses


class LessonForm(ModelForm):
    class Meta:
        model = Lesson


def index(request):
    cour = Courses.objects.all()
    c = {"cour": cour}
    return render(request, 'index.html', c)


def course_view(request, pk):
    course = Courses.objects.get(pk=pk)
    lessons = course.lesson_set.all()
    c = {"course": course, "lessons": lessons}
    return render(request, 'course.html', c)


def course_add(request):
    if request.method == 'POST':
        form = CoursesForm(request.POST)
        if form.is_valid():
            form.save()
            course = form.cleaned_data['name']
            messages.success(request, (u'Новый курс %s был добавлен' % course))
            return redirect('home')
    else:
        form = CoursesForm()
    context = {'form': form}
    return render(request, 'course_add.html', context)


def course_edit(request, pk):
    course = Courses.objects.get(id=int(pk))
    form = CoursesForm(instance=course)
    if request.method == 'POST':
        form = CoursesForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, (u'Информация о курсе %s обновлена' % course.name))
            return redirect('home')
    context = {'form': form,
               'course': course}
    return render(request, 'course_edit.html', context)


def course_delete(request, pk):
    course = Courses.objects.get(id=int(pk))
    if request.method == 'POST':
        course.delete()
        messages.success(request, (u'Курс %s был удален' % course.name))
        return redirect('home')
    context = {'course': course}
    return render(request, 'course_delete.html', context)


def add_lesson(request, pk):
    course = Courses.objects.get(pk=pk)
    form = LessonForm(initial={'course': course})
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, (u'Занятие %s было добавлено на курс %s' %
                                       (form.cleaned_data['thema'], course.name)))
            return redirect('course', pk)
    context = {'form': form,
               'course': course}
    return render(request, 'add_lesson.html', context)