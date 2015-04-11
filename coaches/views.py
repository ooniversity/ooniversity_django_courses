from django.shortcuts import render
from coaches.models import Coach


def coach_detail(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    #lessons = Lesson.objects.filter(course=course).order_by('number')
    #return render(request, 'course_detail.html', {'course': course, 'lessons': lessons})
    return render(request, 'course_detail.html', {'coach': coach})

