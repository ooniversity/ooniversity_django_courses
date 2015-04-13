from django.shortcuts import render
from django.views import generic
from .models import Coach


def coach_d(request, coach_id):
    #coach = Coach.objects.all()
    coach = Coach.objects.get(pk=coach_id)
    return render(request, 'coaches/coaches.html', {'coach': coach})

