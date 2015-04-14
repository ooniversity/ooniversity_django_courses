from django.shortcuts import render

from students.models import Student
from courses.models import Course


def students_list(request):
    course_id = request.GET.get('course_id')

    if course_id is None:
        students = Student.objects.all()
    else:
        course = Course.objects.get(pk=int(course_id))
        students = course.student_set.all()

    return render(request, 'students_list.html', {
        'students': students,
        })


def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    courses = student.courses.all()

    return render(request, 'detail_info.html', {
        'student': student,
        'courses': courses,
        })
