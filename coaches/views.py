# -*- coding: utf-8 -*-
from django.shortcuts import render
from courses.models import Course
from coaches.models import Coach


# Create your views here.
def show_coach_detail(request, id_c):
    id_coach=int(id_c)
    coach = Coach.objects.get(id = id_c)
    courses = Course.objects.all()
    return render(request, 'coaches/coaches.HTML', {'coach': coach,
                                                    'courses': courses,})




    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        courses = Course.objects.all()
        context['courses'] = courses
        return context
