from django.shortcuts import render
from courses.models import Course, Lesson


def main(request):
    courses_list = Course.objects.all().order_by('id')
    return render(request, 'courses/main.html', {'courses_list': courses_list})

def course_info(request, course_id):
    course_qs = Course.objects.filter(id=course_id)
    current_course = course_qs[0]
    lessons_list = Lesson.objects.filter(course__id=course_id).order_by('number_order')
    return render(request, 'courses/course_info.html', {'current_course': current_course, 'lessons_list': lessons_list})

