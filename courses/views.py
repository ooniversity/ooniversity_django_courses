#!/usr/bin/python		
# -*- coding: UTF-8 -*-

from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from students.models import Student
from coaches.models import Coach
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.contrib import messages

# Create your views here.
def course_detail(request, course_id):
    try:
        course_current = Course.objects.get(id=course_id)
        course_name = course_current.name
        course_description = course_current.description
        student_id = str(course_id)
        lessons = Lesson.objects.filter(course=course_current)

        trainer_info = {
            "id": course_current.trainer.id,       
            "fullname": course_current.trainer.user.get_full_name(),
            "description": course_current.trainer.description,
            #"url": "coaches/"+str(course_current.trainer.id)+"/"
        }

        assistant_info = {
            "id": course_current.assistant.id,       
            "fullname": course_current.assistant.user.get_full_name(),
            "description": course_current.assistant.description,
            #"url": "coaches/"+str(course_current.assistant.id)+"/"
        }
        add_lesson_url = "add_lesson"
 
        message = ""
        return render(request, 'courses/course_detail.html', {"lessons": lessons, "message": message, "student_id": student_id, "course_name": course_name, "course_description": course_description, 'trainer_info': trainer_info, 'assistant_info': assistant_info, 'add_lesson_url':add_lesson_url})
    except ObjectDoesNotExist:
        message = "Sorry, no course with id = %s exists yet."%(course_id)
        return render(request, 'course_detail.html', {"message": message})
#https://docs.djangoproject.com/en/1.8/ref/models/querysets/#django.db.models.query.QuerySet.get


class CoursetModification(forms.ModelForm):
    class Meta:
        model = Course


def course_add(request):
    course = Course()
    if request.method == "POST":
        form_add = CoursetModification(request.POST)
        if form_add.is_valid():                
            course = form_add.save()
            messages.success(request, 'Info on a new course successfully added!');
            return redirect("/")
    else:
        form_add = CoursetModification()
    return render(request, 'courses/course_add.html', {"form_add": form_add})

def course_edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form_edit = CoursetModification(request.POST, instance=course)
        if form_edit.is_valid():                
            course = form_edit.save()
            messages.success(request, 'Info on a course has been modified!');
            #return redirect("/")
    else:
        form_edit = CoursetModification(instance=course)
    return render(request, 'courses/course_edit.html', {"form_edit": form_edit})


def course_delete(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        course.delete()
        messages.success(request, "Course %s has been deleted."%(course.name))
        return redirect("/")
    return render(request, 'courses/course_delete.html', {"course": course})



class LessonModification(forms.ModelForm):
    class Meta:
        model = Lesson


def lesson_add(request, course_id):
    lesson = Lesson()
    form_lesson_add = LessonModification()
    if request.method == "POST":
        form_lesson_add = LessonModification(request.POST)
        if form_lesson_add.is_valid():                
            lesson = form_lesson_add.save()
            messages.success(request, 'Info on a new lesson successfully added!');
            return redirect("courses:course", course_id = course_id)
    else:
        form_lesson_add = LessonModification(initial={'course': course_id})
    return render(request, 'courses/lesson_add.html', {"form_lesson_add": form_lesson_add})


