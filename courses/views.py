from django.shortcuts import render
from django.views import generic
from models import Course
from coaches.models import Coach


class IndexView(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'courses_list'

    def get_queryset(self):
        return Course.objects.order_by()

def course_d(request, course_id):
    course = Course.objects.get(pk=course_id)
    coach = Coach.objects.all()
    return render(request, 'courses/courses.html', {'course':course, 'coach':coach})
    
#def courses(request):
    #return render(request,'courses/courses.html')


