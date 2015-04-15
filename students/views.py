from django.shortcuts import render
from django import forms
from students.models import Student


def student_list(request):
    course_id = request.GET.get('course_id')
    if course_id == None:
        students = Student.objects.all()
    else:
        students = Student.objects.filter(courses=course_id)
    return render(request, 'students/student_list.html', {'students': students})


def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    courses = student.courses.all()
    return render(request, 'students/student_detail.html', {'student': student, 'courses': courses})


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student



def student_add(request):
    model_form = StudentForm()
    """
Model forms, 2 video, 2:55
    """
    return render(request, 'students/student_add.html', {'model_form': model_form})

