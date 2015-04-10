from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course, Lesson
from students.models import Student
#from pybursa import urls


def show_index(request):
    courses = Course.objects.all()
    return render(request, 'index.HTML',
                 {'courses': courses})


def show_contacts(request):
    return render(request, 'contact.HTML')


def show_students(request):
    if request.GET.get('course_id') is None:
        students = Student.objects.all()
        return render(request, 'student_list.HTML', {'students': students})
    else:
        students = Student.objects.filter(courses__id = int(request.GET.get('course_id')))
        return render(request, 'student_list.HTML', {'students': students})


def show_student_detail(request, id):
    id_course=int(id)
    student = Student.objects.get(id = id_course)
    return render(request, 'students.HTML', {'student': student})


def show_courses(request, id):
    course = Course.objects.get(id = int(id))
    lessons = Lesson.objects.all()
    lessons = Lesson.objects.filter(course__name = course.name)
    return render(request, 'courses.HTML', {'course': course, 'lessons': lessons})
