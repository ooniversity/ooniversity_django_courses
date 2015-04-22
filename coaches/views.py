# -*- coding: utf-8 -*-
from django.shortcuts import render
from courses.models import Course
from coaches.models import Coach


# Create your views here.
def show_coach_detail(request, id_c):
    id_coach=int(id_c)
    coach = Coach.objects.get(id = id_c)
    return render(request, 'coaches/coaches.HTML', {'coach': coach, })
