from django.shortcuts import render
from courses.models import Course, Lesson

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course=course).order_by('item_no')
    return render(request, 'course_detail.html', {'course': course, 'lessons': lessons})
