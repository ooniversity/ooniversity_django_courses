# -*- coding: utf-8 -*-
from django.shortcuts import render
from courses.models import Course
from coaches.models import Coach


# Create your views here.
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
    return render(request, 'coaches/coaches.HTML', {'coach': coach,
                                                    'teacher': teacher,
                                                    'assistent': assistent})
