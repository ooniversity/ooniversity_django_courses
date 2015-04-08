from django.shortcuts import render
from django.views import generic

from courses.models import Course


class HomeView(generic.ListView):
    template_name = 'index.html'
    model = Course


def contact(request):
    print request
    return render(request, 'contact.html')


def student_list(request):
    return render(request, 'student_list.html')


def student_detail(request):
    return render(request, 'student_detail.html')
