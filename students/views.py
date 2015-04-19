from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages

from students.models import Student
from StudentForm import StudentForm


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

def student_add(request):
    #student = {}
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = form.save()
            messages.success(request, 'added')
            return redirect('students:index')
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {
        #'student': student,
        'form': form,})

def student_edit(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'students/detail.html', {'student': student})

def student_remove(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'students/detail.html', {'student': student})
