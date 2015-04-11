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

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def stud_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", 
                 {'students': students})

def detail(request, student_id):
    qs = Student.objects.all().filter(id=student_id)
    crs = qs[0]

    return render(request, 'students/student_detail.html', {'a': crs, 'lesson': Student.objects.all().filter(courses=student_id)})