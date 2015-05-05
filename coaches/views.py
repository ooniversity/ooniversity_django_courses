from models import Coach
from django.shortcuts import render, get_object_or_404
from courses.models import Course
from pybursa.utils import detail_view

def coach_d(request, pk):
    coach = get_object_or_404(Coach, pk=pk)
    return render(request, 'coaches/detail.html', {'coach': coach})
