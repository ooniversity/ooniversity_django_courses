from django.shortcuts import render
from courses.models import Course, Lesson

def index_courses(request):
    courses = Course.objects.all()

    return render(request, 'index_courses.html', {'courses': courses})


def course_show(request, pk):
    course = Course.objects.get(pk=pk)
    course_lessons = course.lesson_set.all()

    return render(request, 'course_show.html', {
        'course': course,
        'course_lessons': course_lessons,
        })