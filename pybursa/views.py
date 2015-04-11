# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course, Lesson
from students.models import Student
from coaches.models import Coach
#from pybursa import urls


def show_index(request):
    courses = Course.objects.all()
    return render(request, 'index.HTML',
                 {'courses': courses})


def show_contacts(request):
    return render(request, 'contact.HTML')


def show_students(request):
    if request.GET.get('course_id') is None:
        students = Student.objects.all()
        return render(request, 'student_list.HTML', {'students': students})
    else:
        students = Student.objects.filter(courses__id = int(request.GET.get('course_id')))
        return render(request, 'student_list.HTML', {'students': students})


def show_student_detail(request, id):
    id_course=int(id)
    student = Student.objects.get(id = id_course)
    return render(request, 'students.HTML', {'student': student})


def show_courses(request, id):
    course = Course.objects.get(id = int(id))
    lessons = Lesson.objects.filter(course__name = course.name)
    return render(request, 'courses.HTML', {'course': course, 'lessons': lessons})


def show_coach_detail(request, id_c):
    id_coach=int(id_c)
    coach = Coach.objects.get(id = id_c)
    courses = Course.objects.all()
    teacher = []
    assistent = []
    #Формируем список курсов учителя
    for i in courses:
        if coach.user == i.teacher.user:
            teacher.append(i)
    #Формируем список курсов ассистента
    for i in courses:
        if coach.user == i.assistent.user:
            assistent.append(i)
    return render(request, 'coaches.HTML', {'coach': coach, 'teacher': teacher,
                                            'assistent': assistent})
