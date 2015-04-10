from django.shortcuts import render
from django.views import generic

from courses.models import Course, Lesson
from coaches.models import Coach


class CourseView(generic.ListView):
    template_name = 'courses/courses.html'
    model = Course


class CourseDetialView(generic.ListView):
    template_name = 'courses/detail.html'
    model = Lesson

    def get_queryset(self):
        qs = super(CourseDetialView, self).get_queryset()
        course = Course.objects.all().filter(id=self.kwargs['id'])[0]
        coach = Coach.objects.all().filter(user=course.coach.user)[0]
        assistant = Coach.objects.all().filter(user=course.assistant.user)[0]
        return {
            'Lesson': qs.filter(course=self.kwargs['id']).order_by('consecutive_number'),
            'Course': course,
            'Coach': {'coach': coach, 'assistant': assistant}
        }
