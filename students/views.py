from django.shortcuts import render
from django.views import generic

from students.models import Student

class IndexView(generic.ListView):
    template_name = 'students/index.html'
    context_object_name = 'students_list'

    def get_queryset(self):
        return Student.objects.all()

def student(request):
    return render(request, 'students/index.html', {'students_list':Student.objects.all()})

