from students.models import Student
from courses.models import Course, Lesson
from django.views import generic
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    qs = Course.objects.all().filter(id=question_id)
    crs = qs[0]

    return render(request, 'courses/index.html', {'a': crs, 'lesson': Lesson.objects.all().filter(course=question_id)})