from django.shortcuts import render
from django.views import generic

from courses.models import Course
from coaches.models import Coach


class HomeView(generic.ListView):
    template_name = 'index.html'
    model = Course


def contact(request):
    coaches = Coach.objects.all()
    return render(request, 'contact.html', {'coaches': coaches})


def student_list(request):
    return render(request, 'student_list.html')


def student_detail(request):
    return render(request, 'student_detail.html')
