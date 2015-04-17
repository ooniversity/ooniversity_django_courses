from django.shortcuts import render, get_object_or_404

# Create your views here.

from coaches.models import Coach
from courses.models import Course


def coach_info(request, id_coach):
    id_coach_int = int(id_coach)
    coach = get_object_or_404(Coach, id=id_coach_int)
    return render(request, 'coaches/coach_info.html', {'coach': coach})

