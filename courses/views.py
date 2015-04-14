from django.shortcuts import render
from courses.models import Course, Lesson


def index_courses(request):
    courses = Course.objects.all()

    return render(request, 'index_courses.html', {'courses': courses})


def course_show(request, pk):
    course = Course.objects.get(pk=pk)
    course_lessons = course.lessons_list.all()

    coach_info = None
    if course.coach is not None:
        coach_info = {
            'id': course.coach.id,
            'name': course.coach.user.get_full_name(),
            'descr': course.coach.descr,
        }

    assistant_info = None
    if course.assistant is not None:
        assistant_info = {
            'id': course.assistant.id,
            'name': course.assistant.user.get_full_name(),
            'descr': course.assistant.descr,
        }

    return render(request, 'course_show.html', {
        'course': course,
        'course_lessons': course_lessons,
        'coach_info': coach_info,
        'assistant_info': assistant_info,
        })
