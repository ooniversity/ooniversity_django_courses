# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from models import Course, Lesson
from coaches.models import Coach
from django.contrib import messages
from django import forms 

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson

def course_d(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/courses.html', {'course':course})
    
#def courses(request):
    #return render(request,'courses/courses.html')

def add_lesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, 'Студент успешно добавлен', {'lesson':lesson})
            return redirect('courses:courses')
    else:
        form = LessonForm()
    return render(request,'courses/add_lesson.html', {'form':form})

def edit_lesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    form = LessonForm(instance=lesson)

    return render(request,'courses/edit_lesson.html', {'form':form})

def remove_lesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    return render(request,'courses/remove_lesson.html')
