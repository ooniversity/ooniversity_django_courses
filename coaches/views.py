from django.shortcuts import render, get_object_or_404
from coaches.models import Coach
from courses.models import Course


def coach_detail(request, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id)
    courses_coach = Course.objects.filter(coach=coach_id)
    courses_assistant = Course.objects.filter(assistant=coach_id)
    return render(request, 'coaches/coach_detail.html', 
                  {'coach': coach, 'courses_coach': courses_coach, 
                   'courses_assistant': courses_assistant})

