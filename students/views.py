from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Student, Course

def students(request):
    course_id = request.GET['course_id']
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'students/students.html', {'course': course})


