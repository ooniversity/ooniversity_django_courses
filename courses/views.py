# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib import messages

from courses.models import Course, Lesson
from courses.forms import CourseForm, LessonForm


# Current view html-page with coaches

def course_coaches(request, id_course):
    id_course_int = int(id_course)
    course = Course.objects.get(id=id_course_int)
    lessons = Lesson.objects.filter(course__id=course.id)
    return render(request, 'courses/course_coaches.html', {'course': course,
                                                           'lessons': lessons,}
    )


# Views for forms edition course:

# Creation new course
def add_course(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course_app = course_form.save()
            course_mess = u'Курс - {} - успешно добавлен !'.format(course_app.title)
            messages.success(request, course_mess)
            return redirect('index-ooniversity')
    else:
        course_form = CourseForm()
    return render(request, 'courses/add_course.html', {'course_form': course_form})

# Edition course
def edit_course(request, pk_course):
    pk_int = int(pk_course)
    course_app = Course.objects.get(id=pk_int)
    if request.method == 'POST':
        course_form = CourseForm(request.POST, instance=course_app)
        if course_form.is_valid():
            course_app = course_form.save()
            course_mess = u'Данные о курсе - {} - успешно изменены !'.format(course_app.title)
            messages.success(request, course_mess)
            print 'request.path  = ', request.path
            return redirect(request.path)				# ('courses:edit-course' course.id)
    else:
        course_form = CourseForm(instance=course_app)
    return render(request, 'courses/edit_course.html', {'course_form': course_form,
                                                        'course_app': course_app}
    )

# Deletion course
def delete_course(request, pk_course):
    pk_int = int(pk_course)
    course_app = Course.objects.get(id=pk_int)
    if request.method == 'POST':
        course_app.delete()
        course_mess = u'Курс - {} - был успешно удален !'.format(course_app.title)
        messages.success(request, course_mess)
        return redirect('index-ooniversity')
    return render(request, 'courses/delete_course.html', {'course_app': course_app})



# View for form - Creation new lesson:

def add_lesson(request, pk_course):
    pk_int = int(pk_course)
    lesson_course = Course.objects.get(id=pk_int)
    if request.method == 'POST':
        lesson_form = LessonForm(request.POST, initial={'course': lesson_course})
        if lesson_form.is_valid():
            lesson_app = lesson_form.save()
            print 'lesson_app = ', lesson_app
            print 'lesson_course = ', lesson_course
            lesson_mess = u'Занятие - {} - было успешно создано !'.format(lesson_app.theme)
            messages.success(request, lesson_mess)
            # Processing URL path for redirect
            print 'request.path  = ', request.path
            redir_path = request.path
            redir_path = redir_path[:redir_path.rfind('/', 0, -1) + 1]
            print 'redir_path = ', redir_path
            return redirect(redir_path)
    else:
        lesson_form = LessonForm(initial={'course': lesson_course})
    return render(request, 'courses/add_lesson.html', {'lesson_form': lesson_form,
                                                       'lesson_course': lesson_course}
    )
