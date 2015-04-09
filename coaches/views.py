from django.shortcuts import render
from django.views import generic

from coaches.models import Coach
from courses.models import Course


class CoachesView(generic.ListView):
    template_name = 'coaches/coaches.html'
    model = Coach

    def get_queryset(self):
        qs = super(CoachesView, self).get_queryset()
        return {
            'Coach': qs,
            'Course': Course.objects.all(),
        }


class CoachView(generic.ListView):
    template_name = 'coaches/coach.html'
    model = Coach

    def get_queryset(self):
        qs = super(CoachView, self).get_queryset().filter(id=self.kwargs['id'])[0]
        course = Course.objects.all()
        return {
            'Coach': qs,
            'Course_coarch': course.filter(coach=qs),
            'Course_assistant': course.filter(assistant=qs),
        }