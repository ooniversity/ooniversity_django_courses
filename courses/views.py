from django.shortcuts import render
from courses.models import Course, Lesson
from coaches.models import Coach

def course(request, c_id):
    lesson = Lesson.objects.filter(course__id=c_id)
    course = Course.objects.get(id=c_id)
    coach = Coach.objects.filter(user=course.coach.user)[0]
    assistant = Coach.objects.filter(user=course.assistant.user)[0]
    print coach.user.first_name
    d_core = {'crs':course, 'lssn':lesson, 'cch': coach, 'assst':assistant}
    return render(request, 'courses/courses.html', {'courses': d_core})
