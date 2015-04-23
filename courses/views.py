# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib import messages
from django.contrib.messages import get_messages
from django.forms import *

from courses.models import Course, Lesson
from coaches.models import Coach

def course_view(request):
    messages = get_messages(request)
    storage = []
    for message in messages:
        storage.append(message.message)
    messages = storage
    model = Course.objects.all()
    return render_to_response('index.html', {'model': model, 'messages': messages})

def course_plan(request, pk):
    messages = get_messages(request)
    storage = []
    for message in messages:
        storage.append(message.message)
    messages = storage
    planmodel = Course.objects.get(pk=pk)
    lessons = planmodel.coursekey.all().order_by('order_number')
    course = Course.objects.all().filter(id=pk)[0]
    coach = Coach.objects.all().filter(user=course.coach.user)
    assistant = Coach.objects.all().filter(user=course.assistant.user)
    return render_to_response('courses.html', {
        'planmodel': planmodel,
        'lessons': lessons, 'messages': messages,
        'coach': [coach[0], coach[0].descr],
        'assistant': [assistant[0], assistant[0].descr],
        })


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


def course_add(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, u"Курс %s был успешно добавлен!" % course.name)
            return redirect('main')
    else:
        form = CourseForm()
    return render(request, 'cadd_edit.html', {'form': form,})


def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course.update_data(**form.cleaned_data)
            course.save()
            messages.success(request, u"Данные изменены!")
            return redirect('courses:course_edit', pk)
    else:
        form = CourseForm(instance=course)
    return render(request, 'cadd_edit.html', {'form': form})


def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    print Course
    if request.method == "POST":
        course.delete()
        messages.success(
            request, u"Курс %s был удалён" % course.name)
        return redirect('main')
    else:
        return render(request, 'cdelete.html', {'course': course})


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