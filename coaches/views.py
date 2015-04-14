from django.shortcuts import render
from courses.models import Course
from coaches.models import Coach
from students.models import Student
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def detail(request, coach_id):
    qs = Coach.objects.all().filter(id=coach_id)
    crs = qs[0]

    return render(request, 'coaches/coaches.html', {'a': crs})

