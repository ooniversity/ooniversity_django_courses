from django.shortcuts import render
from courses.models import Course, Lesson
from students.models import Student

from django.views.generic import TemplateView


def home(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})


class ContactViews(TemplateView):
    template_name = 'contact.html'


def contact(request):
    return render(request, 'contact.html')


def student_list(request):
    return render(request, 'student_list.html')


def student_detail(request):
    return render(request, 'student_detail.html')