# -*- coding: utf-8 -*- 

from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course

def coach(request, coa):
    cch = Coach.objects.get(user_id = coa)
    text1 = ''
    text2 = ''
    crs_teacher = Course.objects.filter(coach = cch)
    if crs_teacher:
        text1 = "Курсы учитель: "
    crs_assist = Course.objects.filter(assistant = cch)
    if crs_assist:
        text2 = "Курсы ассистент: "
    d = {'cch':cch, 'crs_teacher': crs_teacher, 'crs_assist': crs_assist, 'text':[text1, text2]}
    return render(request, 'coaches/coach.html', {'dd':d})

