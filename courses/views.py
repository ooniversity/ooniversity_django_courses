from django.shortcuts import render
from models import Course, Lesson, Coach

def course_info(request, id):
    courses = Course.objects.get(id=id)
    lessons = Lesson.objects.filter(course_id=id)
    course = Course.objects.filter(id=id)[0]
    #course = Course.objects.get(id=id)
    coach = Coach.objects.filter(user=course.coach.user)
    assistant = Coach.objects.filter(user=course.assistant.user)

    return render(request, 'courseinfo.html', {'courses': courses, \
            'lessons': lessons, 'coach': [coach[0], coach[0].description],\
             'assistant': [assistant[0], assistant[0].description]})

