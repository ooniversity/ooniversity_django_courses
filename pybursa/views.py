from django.shortcuts import render
from courses.models import Course, Lesson



def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course=course)
    return render(request, 'course_detail.html', {'course': course, 'lessons': lessons})


