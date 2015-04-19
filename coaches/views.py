#!/usr/bin/python		
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from courses.models import Course, Lesson
from students.models import Student
from coaches.models import Coach
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def coach_detail(request, co_id):
    try:
        coaches = Coach.objects.get(id=co_id)
        message = ""
        coaches_info = {
            "fullname": coaches.user.get_full_name(),
            "date": coaches.birth_date,
            "address": coaches.address,
            "scype": coaches.scype,
            "phone": coaches.phone,
            #"email": coaches.user.email(),
            "courses_trainer": coaches.rel_trainers.all(),
            "courses_assistant": coaches.rel_assistants.all(),
            }    
        return render(request, 'coaches/coach.html', {"coaches": coaches, "coaches_info": coaches_info})
    except ObjectDoesNotExist:
        message = "Sorry, no coach with id = %s exists yet."%(co_id)
        return render(request, 'coaches/coach.html', {"message": message})

