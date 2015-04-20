from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def coach_info(request, id):
    coach = Coach.objects.get(pk=id)

    return render(request, 'coach_detail.html', {'coach': coach})
