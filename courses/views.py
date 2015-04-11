from django.shortcuts import render
from models import Course, Lesson

def course_info(request, id):
    courses = Course.objects.get(id=id)
    lessons = Lesson.objects.filter(course_id=id)
    print lessons
    return render(request, 'courseinfo.html', {'courses': courses, 'lessons': lessons})
