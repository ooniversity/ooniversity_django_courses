from django.shortcuts import render
from courses.models import Courses, Lesson


def index(request):
    cour = Courses.objects.all()
    c = {"cour": cour}
    return render(request, 'index.html', c)


def course_view(request, pk):
    one_c = Courses.objects.get(id__exact=int(pk))
    lessons = Lesson.objects.filter(course__id__exact=int(pk))
    print one_c.trener.desc
    c = {"course": one_c, "lessons": lessons}
    return render(request, 'course.html', c)
