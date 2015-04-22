# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from django import forms
from django.contrib import messages


#Создаем форму для веб браузера на основе модели Course
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        #Указываем поля, которые не нужно выводить пользователю


#Создаем форму для веб браузера на основе модели Course
class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        #Указываем поля, которые не нужно выводить пользователю


# Create your views here.
def show_courses(request, pk):
    course = Course.objects.get(id = pk)
    lessons = Lesson.objects.filter(course__name = course.name)
    return render(request, 'courses/courses.HTML', {'course': course, 'lessons': lessons})


#Вьюшка для создания нового курса
def create_course(request):
    if request.method == 'POST':
        #Инстанцирование формы для студента
        model_form = CourseForm(request.POST)
        if model_form.is_valid():
            application = model_form.save()
            messages.success(request, u'Курс {} успешно добавлен'.format(application.name))
            return redirect ('/')
    else:
        model_form = CourseForm()
    return render(request, 'courses/new_course.HTML',
                  {'model_form':model_form})


#Вьюшка для создания нового урока
def create_lesson(request, pk):
    if request.method == 'POST':
        #Инстанцирование формы для урока
        model_form = LessonForm(request.POST)
        if model_form.is_valid():
            application = model_form.save()
            messages.success(request, u'Урок {} для курса {} успешно добавлен'.format(application.theme, application.course.name))

            return redirect ('courses:course', application.course_id)
    else:
        model_form = LessonForm(initial={'course':pk,})
    return render(request, 'courses/new_lesson.HTML',
                  {'model_form':model_form})


#Вьюшка для редактирования нового курса
def edit_course(request, pk):
    application = Course.objects.get(id=pk)
    if request.method == 'POST':
        model_form = CourseForm(request.POST, instance=application)
        if model_form.is_valid():
            application = model_form.save()
            messages.success(request, u'Данные о курсе {} успешно изменены'.format(application.name))

            return redirect (request.path)
    else:
        model_form = CourseForm(instance=application)
    return render(request, 'courses/edit_data_course.HTML',
                  {'model_form':model_form})


#Вьюшка для редактирования нового урока
def edit_lesson(request, pk):
    application = Course.objects.get(id=pk)
    if request.method == 'POST':
        model_form = LessonForm(request.POST, instance=application)
        if model_form.is_valid():
            application = model_form.save()
            messages.success(request, u'Данные {} для урока {} изменены'.format(application.theme,
                                                                                application.course.name))
            return redirect (request.path)
    else:
        model_form = LessonForm(instance=application)
    return render(request, 'courses/edit_data_lesson.HTML',
                  {'model_form':model_form})


#Вьюшка для удаления курса
def remove_course(request, pk):
    application = Course.objects.get(id=pk)
    if request.method == 'POST':
        application.delete()
        messages.success(request, u'Курс {} был удален'.format(application.name))
        return redirect ('index_itbursa')
    return render(request, 'courses/remove_course.HTML',
                  {'course':application})


#qs = Lesson.objects.get(id=pk)
#Вьюшка для удаления урока
#def remove_lesson(request, pk):
#    application = Lesson.objects.get(id=pk)
#    if request.method == 'POST':
#        application.delete()
#        messages.success(request, u'Урок {} был удален'.format(application.theme))
#        return redirect (request.path[:request.path.find(pk)+1])
#    return render(request, 'courses/remove_course.HTML',
#                  {'course':application})
