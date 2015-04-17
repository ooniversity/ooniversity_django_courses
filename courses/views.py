# -*- coding: utf-8 -*-

from datetime import datetime
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from courses.models import Course, Lesson


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course=course).order_by('number')
    return render(request, 'courses/course_detail.html', 
                  {'course': course, 'lessons': lessons})


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


def course_add(request):
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
            return render(request, 'courses/course_add.html', {'form': form})
    else:
        form = CourseForm()   
    return render(request, 'courses/course_add.html', {'form': form})


def course_edit(request, course_id):
    course = Course.objects.get(id=course_id)
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
                          'courses/course_edit.html', {'form': form})
    else:
        form = CourseForm(instance=course)   
    return render(request, 'courses/course_edit.html', {'form': form})


def course_remove(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        name = course.name
        course.delete()
        messages.success(request,u'Курс "{0}" был удалён'\
                         .format(name))
        return redirect('index')
    return render(request, 'courses/course_remove.html', {'course': course})
