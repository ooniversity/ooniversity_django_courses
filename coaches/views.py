from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course

def coach_info(request, id):
    planmodel = Course.objects.get(pk=id)
    coach = Coach.objects.get(pk=id)
    coursecoach = coach.coachkey.all()
    courseassist = coach.assistantkey.all()
    return render('coach_details.html', {'coach': coach,
        'coursecoach': coursecoach,
        'courseassist': courseassist,
        'planmodel': planmodel,
        })