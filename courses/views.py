# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from coaches.models import Coach
from django import forms
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView



#class CourseView(TemplateView):
#    template_name = 'courses/courses.html'


class CourseDetailView(DetailView):
    model = Course


class CourseListView(ListView):
    model = Course


def course(request, c_id):
    lessons = Lesson.objects.filter(course__id=c_id)
    course = Course.objects.get(id=c_id)
    coach = Coach.objects.get(user=course.coach.user)
    assistant = Coach.objects.get(user=course.assistant.user)
    print coach.user.first_name
    d_core = {'course':course, 'lessons':lessons, 'coach': coach, 'assistant':assistant}
    return render(request, 'courses/courses.html', d_core)


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson



def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            new_course = form.save()
            messages.success(request, u"Курс {0} успешно создан".format(new_course.name))
            return redirect('index')
        else:
            return render(request, 'courses/add_course.html', {'form': form}) 

    else:
        form = CourseForm()

    return render(request, 'courses/add_course.html', {'form': form})



def edit_course(request, id):
    course = Course.objects.get(pk=id)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, u"Данные изменены.")
            return redirect('courses:courses', id)
        else:
            return render(request, 'courses/edit_course.html', {'form': form}) 

    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/edit_course.html', {'form': form})


def remove_course(request, id):
    course = Course.objects.get(pk=id)
    if request.method == 'POST':
        course.delete()
        messages.success(request,u"Студент {0} был удалён".format(course.name))
        return redirect('index')
    
    return render(request, 'courses/remove_course.html', {'course':course})



def add_lesson(request, id):
    course = Course.objects.get(pk=id)
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            new_lesson = Lesson()
            new_lesson.course = course
            new_lesson = form.save()
            messages.success(request, u"Занятие {0} успешно создано".format(new_lesson.theme))
            return redirect('courses:courses', id)
        else:
            return render(request, 'courses/add_lesson.html', {'form': form}) 

    else:
        form = LessonForm(initial={'course':course})

    return render(request, 'courses/add_lesson.html', {'form': form}) 












