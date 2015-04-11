from django.shortcuts import render
from django.views import generic

from coaches.models import Coach
from courses.models import Course


class CoachesView(generic.ListView):
    template_name = 'coaches/coaches.html'
    model = Coach


class CoachView(generic.ListView):
    template_name = 'coaches/coach.html'
    model = Coach

    def get_queryset(self):
        qs = super(CoachView, self).get_queryset().filter(id=self.kwargs['id'])
        return qs
