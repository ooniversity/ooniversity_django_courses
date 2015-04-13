from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course

def coach_info(request, id):
    init = Course.objects.get(pk=id)
    coach = Coach.objects.get(pk=id)
    coursecoach = coach.coachh.all()
    courseassist = coach.assistantt.all()
    return render(request, 'coach_detail.html', {'coach': coach,
        'coursecoach': coursecoach,
        'courseassist': courseassist,
        'init': init,
        })