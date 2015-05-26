# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib import auth
from courses.models import Course
from coaches.models import Coach
from django.views.generic.list import ListView


# Create your views here.
def show_coach_detail(request, id_c):
    id_coach=int(id_c)
    coach = Coach.objects.get(id = id_c)
    courses = Course.objects.all()
    return render(request, 'coaches/coaches.HTML', {'coach': coach,
                                                    'courses': courses,
                                                    'username': auth.get_user(request).username,})

 #С помощью класса ListView выводим список преподавателей на HTML страничку
class CoachListView(ListView):
    model = Coach

    def get_context_data(self, **kwargs):
        context = super(CoachListView, self).get_context_data(**kwargs)
        courses = Course.objects.all()
        context['courses'] = courses
        context['username'] = auth.get_user(self.request).username
        return context
