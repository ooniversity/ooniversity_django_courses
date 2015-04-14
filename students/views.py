from django.shortcuts import render
from django.views import generic

from students.models import Student


def index(request):
    pk = request.GET.get('course_id')
    if pk:
        linked_students = Student.objects.filter(courses=int(pk))
    else:
        linked_students = Student.objects.all()
    return render(request, 'students/index.html', {'student_list': linked_students})

def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'students/detail.html', {'student': student})
