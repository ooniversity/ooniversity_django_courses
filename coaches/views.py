# -*- coding: utf-8 -*- 

from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course

def coach(request, coach_id):
    coach = Coach.objects.get(user_id=coach_id)
    teacher_courses = Course.objects.filter(coach=coach)
    assistant_courses = Course.objects.filter(assistant=coach)
    d = {'coach':coach, 'teacher_courses': teacher_courses, 'assistant_courses': assistant_courses}
    return render(request, 'coaches/coach.html', d)

