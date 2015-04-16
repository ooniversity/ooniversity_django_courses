from django.shortcuts import render
from students.models import Student


def students(request):
    course_id = request.GET.get('course_id')
    if course_id == None:
        students = Student.objects.all()
    else:
        students = Student.objects.filter(course=course_id)
    return render(request, 'student_list.html', {'students': students})

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    courses = student.course.all()
    return render(request, 'student_detail.html', {'student': student, 'courses': courses})

