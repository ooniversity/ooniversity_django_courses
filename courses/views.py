from django.shortcuts import render
from courses.models import Course, Lesson

def course(request, c_id):
    lesson = Lesson.objects.filter(course__id=c_id)
    course = Course.objects.get(id=c_id)
    d_core = {'crs':course, 'lssn':lesson}
    return render(request, 'courses/courses.html', {'courses': d_core})
