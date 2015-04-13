from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def coach_info(request, coach_id):
    coach = Coach.objects.get(pk=coach_id)
    course_instructor = Course.objects.filter(instructor=coach_id)
    course_assistant = Course.objects.filter(assistant=coach_id)
    return render(request, 'coach_info.html', {'coach': coach,
                                               'course_instructor': course_instructor,
                                               'course_assistant': course_assistant})
