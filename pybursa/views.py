from django.shortcuts import render
from courses.models import Course, Lesson
from students.models import Student



def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    course_id = request.GET.get('course_id')
    if course_id == None:
        students = Student.objects.all()
    else:
        students = Student.objects.filter(courses=course_id)
    return render(request, 'student_list.html', {'students': students})

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    courses = student.courses.all()
    return render(request, 'student_detail.html', {'student': student, 'courses': courses})

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course=course)
    return render(request, 'course_detail.html', {'course': course, 'lessons': lessons})


