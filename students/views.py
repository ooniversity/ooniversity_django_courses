from django.shortcuts import get_object_or_404,render
from django.views import generic

from students.models import Student


def student(request):
    if request.GET.get('course_id'):
        course_id = int(request.GET.get('course_id'))
        students_list = Student.objects.filter(course=course_id)
    else:
        students_list = Student.objects.all()
    return render(request, 'students/index.html', {'students_list': students_list})


def student_detail(request, question_id):
    student = get_object_or_404(Student, pk=question_id)
    template_name = 'students/detail_student.html'
    return render(request, template_name, {'student': student})
