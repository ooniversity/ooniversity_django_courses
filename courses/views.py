from django.shortcuts import render
from django.views import generic
from .models import Course, Lesson

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'courses_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Course.objects.order_by()

class DetailView(generic.DetailView):
    model = Course
    template_name = 'courses/courses.html'

#def courses(request):
    #return render(request,'courses/courses.html')


