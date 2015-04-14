from django.shortcuts import render
from students.models import Student


# Create your views here.
def show_students(request):
    if request.GET.get('course_id') is None:
        students = Student.objects.all()
        return render(request, 'students/student_list.HTML', {'students': students})
    else:
        students = Student.objects.filter(courses__id = int(request.GET.get('course_id')))
        return render(request, 'students/student_list.HTML', {'students': students})


def show_student_detail(request, id):
    id_course=int(id)
    student = Student.objects.get(id = id_course)
    return render(request, 'students/students.HTML', {'student': student})
