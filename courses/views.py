from django.shortcuts import render, get_object_or_404
from django.views import generic
from models import Course
from coaches.models import Coach

def course_d(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/courses.html', {'course':course})
    
#def courses(request):
    #return render(request,'courses/courses.html')


