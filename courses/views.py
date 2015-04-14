from django.shortcuts import render
from courses.models import Course, Lesson


def index_courses(request):
    courses = Course.objects.all()
    return render(request, 'index_courses.html', {'courses': courses})


def course_description(request, course_id):
    course = Course.objects.get(pk=course_id)
    lessons = Lesson.objects.filter(course=course).order_by('number')
    return render(request, 'course_detail.html', {'course': course, 'lessons': lessons})
