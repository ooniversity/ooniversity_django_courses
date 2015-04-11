#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from courses.models import Course, Lesson
from students.models import Student
from django.template import RequestContext, loader
from django.http import HttpResponse, Http404


def index(request):

    course_list = Course.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'course_list': course_list,
    })
    return HttpResponse(template.render(context))


#    return render_to_response('index.html')

def contacts(request):
#    return HttpResponse("You're looking at poll %s." % poll_id)
    return render_to_response('contacts.html')

def student_list(request, course_id=None):
    if course_id:
        student_list = Student.objects.filter(student_course=course_id)
        course_list = Course.objects.get(pk=course_id)
        template = loader.get_template('student_list.html')
    else:
        student_list = Student.objects.all()
        course_list = Course.objects.all()
        template = loader.get_template('students.html')

    context = RequestContext(request, {
        'student_list': student_list,
        'course_list': course_list,
    })

    return HttpResponse(template.render(context))

def students(request):

    student_list = Student.objects.all()
    course_list = Course.objects.all()

    template = loader.get_template('students.html')
    context = RequestContext(request, {
        'student_list': student_list,
        'course_list': course_list,
    })

    return HttpResponse(template.render(context))

def student_detail(request, student_id):
    student_list = Student.objects.get(pk=student_id)
    course_list = Course.objects.filter(student=student_id)
    template = loader.get_template('student_detail.html')
    context = RequestContext(request, {
        'student_list': student_list,
        'course_list': course_list,
    })
    return HttpResponse(template.render(context))



def course(request, course_id):

    course_list = Course.objects.get(pk=course_id)
    lesson_list = Lesson.objects.filter(lesson_course=course_id)
    template = loader.get_template('course.html')
    context = RequestContext(request, {
        'course_list': course_list,
        'lesson_list': lesson_list,
    })

    return HttpResponse(template.render(context))
