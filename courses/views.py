from django.shortcuts import render
from django.views import generic

from courses.models import Course, Lesson


class CourseView(generic.ListView):
    template_name = 'courses/courses.html'
    model = Course


class CourseDetialView(generic.ListView):
    template_name = 'courses/detail.html'
    model = Lesson

    def get_queryset(self):
        qs = super(CourseDetialView, self).get_queryset()
        return {'Lesson': qs.filter(course=self.kwargs['id']).order_by('consecutive_number'),
                'Course': Course.objects.filter(id=self.kwargs['id'])[0],
        }
