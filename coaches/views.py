from django.shortcuts import render
from models import Coach
from courses.models import Course


def coach_d(request, coach_id):
    coach = Coach.objects.get(pk=coach_id)
    return render(request, 'coaches/coaches.html', {'coach': coach})
