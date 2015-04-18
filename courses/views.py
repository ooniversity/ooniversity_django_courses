# -*- coding: UTF-8 -*-

from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import Course, Lesson


def main(request):
    courses_list = Course.objects.all().order_by('id')
    return render(request, 'courses/main.html', {'courses_list': courses_list})

def course_info(request, course_id):
    current_course = Course.objects.get(id=course_id)
    lessons_list = Lesson.objects.filter(course__id=course_id).order_by('number_order')
    return render(request, 'courses/course_info.html', {'current_course': current_course, 'lessons_list': lessons_list})

def contacts(request):
    return render(request, 'courses/contacts.html')


class CourseApplicationForm(forms.ModelForm):
    class Meta:
        model = Course


def course_add(request):
    if request.method == 'POST':
        form = CourseApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(request, u'Курс %s успешно добавлен' %(application.name))
            return redirect('main')
    else:
        form = CourseApplicationForm()
    return render(request, 'courses/course_add.html', {'form': form})

def course_edit(request, course_id):
    application = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseApplicationForm(request.POST, instance=application)
        if form.is_valid():
            application = form.save()
            messages.success(request, u'Данные о курсе %s изменены' %(application.name))
            return redirect('courses:course_edit', application.id)
    else:
        form = CourseApplicationForm(instance=application)
    return render(request, 'courses/course_edit.html', {'form': form, 'application': application})

def course_remove(request, course_id):
    application = Course.objects.get(id=course_id)
    if request.method == 'POST':
        application.delete()
        messages.success(request, u'Курс %s удален' %(application.name))
        return redirect('main')
    return render(request, 'courses/course_remove.html', {'application': application})




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
        form = LessonApplicationForm()
    return render(request, 'courses/add_lesson.html', {'form': form})