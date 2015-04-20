from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def coach_show(request, pk):
    coach_info = Coach.objects.get(pk=pk)

    return render(request, 'coach_show.html', {
        'coach_info': coach_info,
    })
