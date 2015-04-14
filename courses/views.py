from django.shortcuts import render
from django.views import generic

from courses.models import Course, Lesson
from coaches.models import Coach


class CourseView(generic.ListView):
    template_name = 'courses/courses.html'
    model = Course


class CourseDetialView(generic.ListView):
    template_name = 'courses/detail.html'
    model = Course

    def get_queryset(self):
        qs = super(CourseDetialView, self).get_queryset().filter(id=self.kwargs['id'])
        return qs
