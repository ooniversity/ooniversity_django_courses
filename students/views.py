from django.shortcuts import render
from django.views import generic
from .models import Student

class IndexView(generic.ListView):
    template_name = 'students/students.html'
    context_object_name = 'students_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Course.objects.order_by("index_number")

class DetailView(generic.DetailView):
    model = Course
    template_name = 'students/students.html'
