from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import Http404

from courses.models import Course, Lesson, CourseForm, LessonForm


def index_courses(request):
    courses = Course.objects.all()

    return render(request, 'index_courses.html', {'courses': courses})


def course_show(request, pk):
    course = Course.objects.get(pk=pk)
    course_lessons = course.lessons_list.all()

    coach_info = None
    if course.coach is not None:
        coach_info = {
            'id': course.coach.id,
            'name': course.coach.user.get_full_name(),
            'descr': course.coach.descr,
        }

    assistant_info = None
    if course.assistant is not None:
        assistant_info = {
            'id': course.assistant.id,
            'name': course.assistant.user.get_full_name(),
            'descr': course.assistant.descr,
        }

    return render(request, 'course_show.html', {
        'course': course,
        'course_lessons': course_lessons,
        'coach_info': coach_info,
        'assistant_info': assistant_info,
        })


def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == "POST":
        course.delete()
        messages.success(
            request, u"Course: {} was deleted".format(
                course.title))
        return redirect('home')

    return render(request, 'course_delete.html', {
        'course': course,
    })


def course_add(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(
                request, u"Course {} add success!".format(
                    course.title))
            return redirect('home')
    else:
        form = CourseForm()

    return render(request, 'course_add.html', {
        'form': form,
    })


def course_edit(request, pk):
    course = Course.objects.get(id=pk)

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course.save()
            messages.success(
                request, u"{} update success!".format(
                    course.title))
            return redirect('home')
    else:
        form = CourseForm(instance=course)

    return render(request, 'course_edit.html', {
        'form': form,
    })


