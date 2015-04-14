from django.shortcuts import render
from students.models import Student

def students_all(request):
    if not request.GET.get('course_id'):
        students_all = Student.objects.all().order_by('surname')
        return render(request, 'students/students_all.html', {'students_all': students_all})
    else:
        course_num = request.GET.get('course_id')
        students_all = Student.objects.filter(courses=course_num).order_by('surname')
        return render(request, 'students/students_all.html', {'students_all': students_all})


def student_info(request, student_id):
    student_info = Student.objects.get(id=student_id)
    return render(request, 'students/student_info.html', {'student_info': student_info})
