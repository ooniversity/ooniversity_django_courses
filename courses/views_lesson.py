# coding=utf-8
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import messages

from courses.models import Course, Lesson
from CourseForm import CourseForm, LessonForm



def item_add(request, pk):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            new_item = form.save()
            info_message = 'Занятие ' + str(new_item.title) + ' успешно добавлено'
            messages.success(request, info_message)
            return redirect('courses:detail', pk=pk)
    else:
        form = LessonForm(initial={'course': pk})
    action_name = "   Создать   "

    return render(request, 'courses/add_lesson.html', {
        'form': form,
        'action_name': action_name,})
