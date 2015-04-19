# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.db.models import Max
from django.http import HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse

from models import Course, Lesson


class LessonAddingForm(forms.ModelForm):

    class Meta:
        model = Lesson


def course_info(request, id):
    course = Course.objects.get(pk=id)
    lessons = Lesson.objects.filter(course=course)

    return render(request, 'courseinfo.html', {'course': course, 'lessons': lessons})


def lesson_adding(request, id):
    if request.method == "POST":
        form = LessonAddingForm(request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            application = form.save()
            messages.add_message(request, messages.INFO, 'Новое занятие "' + str(clean.get('theme')) +
                                 '" успешно добавлено' )
            return HttpResponsePermanentRedirect(reverse('courses:courseinfo', args=(id)))

    else:
        lessons = Lesson.objects.filter(course_id=id)
        maxlessonnum = lessons.aggregate(Max('num'))    # определяем максимальный номер урока на курсе
        nextNum = maxlessonnum['num__max'] + 1          # предлагаем сохранить урок под след. номером после максимального

        form = LessonAddingForm(initial={'course': id, 'num': nextNum })
    return render(request, 'add_course.html', {'form': form})
