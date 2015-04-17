from django.shortcuts import render

# Create your views here.

from students.models import Student


def students(request):
    if request.GET.get('course_id') != None:
        request_int = int(request.GET.get('course_id'))
        students = Student.objects.filter(courses__id=request_int)
        return render(request, 'students/students.html', {'students': students})
    else:
        students = Student.objects.all()
        return render(request, 'students/students.html', {'students': students})

def student_info(request, id_stud):
    id_stud_int = int(id_stud)
    student = Student.objects.get(id=id_stud_int)
    return render(request, 'students/student_info.html', {'student': student})

