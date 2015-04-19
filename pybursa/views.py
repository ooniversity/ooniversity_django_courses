from django.shortcuts import render
from courses.models import Course
from django.views.generic import TemplateView


def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})


def student_l(request):
    return render(request, 'student_list.html')
