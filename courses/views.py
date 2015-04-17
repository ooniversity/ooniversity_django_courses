from django.shortcuts import render
from models import Course, Lesson, Coach


def course_info(request, id):
    course = Course.objects.get(pk=id)
    lessons = Lesson.objects.filter(course=course)

    return render(request, 'courseinfo.html', {'course': course, 'lessons': lessons})
