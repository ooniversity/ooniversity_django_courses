from django.shortcuts import render

# Create your views here.

from courses.models import Course, Lesson


# Current view html-page with coaches

def course_coaches(request, id_course):
    id_course_int = int(id_course)
    course = Course.objects.get(id=id_course_int)
    lessons = Lesson.objects.filter(course__id=course.id)
    return render(request, 'courses/course_coaches.html', {'course': course,
                                                           'lessons': lessons,}
    )
