from students.models import Student
from courses.models import Course, Lesson
from django.views import generic
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms
from django.contrib import messages

class CourseLessonForm(forms.ModelForm):
    class Meta:
        model = Lesson

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    crs = Course.objects.all().filter(id=question_id)[0]
    return render(request, 'courses/index.html', {'course': crs, 'lesson': Lesson.objects.all().filter(course=question_id)})

def add_lesson_to_course(request, question_id):
    if request.method == 'POST':
        form = CourseLessonForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(request, "Lesson added!")
            return redirect('/')
    else:
        form = CourseLessonForm()
    return render(request, "courses/apply.html", {'form': form})

def edit_lesson_in_course(request, question_id):
    application = Lesson.objects.get(id=question_id)
    if request.method == 'POST':
        form = CourseLessonForm(request.POST, instance=application)
        if form.is_valid():
            application = form.save()
            messages.success(request, "Lesson saved!")
            return redirect('/')
    else:
        form = CourseLessonForm()   
    form = CourseLessonForm(instance=application)
    return render(request, "courses/edit.html", {'form': form})

def delete_lesson_from_course(request, question_id):
    application = Lesson.objects.get(id=question_id)
    if request.method == 'POST':
        application.delete()
        messages.success(request, "Lesson Removed!")
        return redirect('/')
    return render(request, "courses/delete.html", {'application': application})