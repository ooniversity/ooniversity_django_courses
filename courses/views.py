# -*- coding: utf-8 -*-

from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.contrib import messages
from courses.models import Course, Lesson


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.filter(course=course).order_by('number')
    return render(request, 'courses/course_detail.html', 
                  {'course': course, 'lessons': lessons})


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


def course_add(request):
    page_title = u"Создание нового курса"
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            new_course = Course()
            new_course = form.save()
            messages.success(request, 
                             u'Курс "{0}" успешно добавлен'\
                              .format(new_course.name))
            return redirect('index')
        else:
            return render(request, 'add_edit.html', {'form': form, 'page_title':page_title})
    else:
        form = CourseForm()   
    return render(request, 'add_edit.html', {'form': form, 'page_title':page_title})


def course_edit(request, course_id):
    page_title = u"Редактирование курса"
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, 
                            u"Изменения данных курса сохранены в {0}"\
                             .format(datetime.now().strftime("%H:%M:%S")))
            return redirect('courses:course_edit', course_id)
        else:
            return render(request, 
                          'add_edit.html', {'form': form, 'page_title':page_title})
    else:
        form = CourseForm(instance=course)   
    return render(request, 'add_edit.html', {'form': form, 'page_title':page_title})


def course_remove(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    name = course.name
    page_title = u"Удаление курса"
    page_header = u'Курс "{0}" будет удалён'.format(name)
    if request.method == 'POST':
        course.delete()
        messages.success(request,u'Курс "{0}" был удалён'\
                         .format(name))
        return redirect('index')
    return render(request, 'remove.html', {'page_title':page_title, 'page_header':page_header})


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'


def lesson_add(request, course_id):
    page_title = u"Создание нового занятия"
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            new_lesson = Lesson()
            new_lesson = form.save()
            messages.success(request, 
                             u'Занятие "{0}" успешно добавлено'\
                              .format(new_lesson.theme))
            return redirect('courses:course_detail', course_id=course_id)
        else:
            return render(request, 'add_edit.html', {'form': form, 'page_title':page_title})
    else:
        form = LessonForm(initial={'course':course})   
    return render(request, 'add_edit.html', {'form': form, 'page_title':page_title})
