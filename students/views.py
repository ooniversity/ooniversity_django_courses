from django.shortcuts import render
from students.models import Student


def student (request):
    students = Student.objects.all()
    return render(request, 'students_list.html', 
                  {'students':students})
