from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def coach_show(request, pk):
    coach_info = Coach.objects.get(pk=pk)

    coach_name = coach_info.user.get_full_name()

    coach_courses = coach_info.courses_as_coach.all()

    assistant_courses = coach_info.courses_as_assistant.all()

    return render(request, 'coach_show.html', {
        'coach_info': coach_info,
        'coach_name': coach_name,
        'coach_courses': coach_courses,
        'assistant_courses': assistant_courses,
    })
