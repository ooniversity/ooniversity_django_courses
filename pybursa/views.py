from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course, Lesson
from students.models import Student
#from pybursa import urls

def show_index(request):
    courses = Course.objects.all()
    return render(request, 'index.HTML',
        {'courses':courses})

def show_contacts(request):
    return render(request, 'contact.HTML')

def show_students(request):
    students = Student.objects.all()
    print students[3].courses, 'helloS'
    return render(request, 'student_list.HTML',
        {'students':students}   )

def show_student_detail(request, id):
    id_course=int(id)
    student = Student.objects.get(id = id_course)
    return render(request, 'students.HTML',
        {'student':student})

def show_courses(request, id):
    id_course=int(id)
    course = Course.objects.get(id = id_course)
    lessons = Lesson.objects.all()
    list=[]
    for x in range(len(lessons)):
        if str(lessons[x].course) == str(course.name):
            list.append(lessons[x].id)
    lessons = Lesson.objects.filter(id__in=list)
    return render(request, 'courses.HTML',
        {'course':course, 'lessons':lessons})
