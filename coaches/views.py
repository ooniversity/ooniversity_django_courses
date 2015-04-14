from django.shortcuts import render_to_response
from coaches.models import Coach
from courses.models import Course

def coach(request, pk):
    planmodel = Course.objects.get(pk=pk)
    coach = Coach.objects.get(pk=pk)
    coursecoach = coach.coachkey.all()
    courseassist = coach.assistantkey.all()
    return render_to_response('coach_details.html', {'coach': coach,
        'coursecoach': coursecoach,
        'courseassist': courseassist,
        'planmodel': planmodel,
        })
