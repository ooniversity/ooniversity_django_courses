from django.shortcuts import render
from courses.models import Course, Lesson


# Create your views here.
def show_courses(request, id):
    course = Course.objects.get(id = int(id))
    lessons = Lesson.objects.filter(course__name = course.name)
    return render(request, 'courses/courses.HTML', {'course': course, 'lessons': lessons})
