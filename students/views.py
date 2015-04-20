# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib import messages

from students.models import Student
from students.forms import StudentForm


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



# Views for forms edition student:

# Creation new student
def add_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_app = student_form.save()
#            student_mess = u'Студент - {} - успешно добавлен !'.format(student_app.full_name)
            student_mess = u'Студент - {} {} - успешно добавлен !'.format(student_app.name,
                                                                          student_app.surname)
            messages.success(request, student_mess)
            return redirect('students:student-list')
    else:
        student_form = StudentForm()
    return render(request, 'students/add_student.html', {'student_form': student_form})

# Edition student
def edit_student(request, pk_stud):
    pk_int = int(pk_stud)
    student_app = Student.objects.get(id=pk_int)
    if request.method == 'POST':
        student_form = StudentForm(request.POST, instance=student_app)
        if student_form.is_valid():
            student_app = student_form.save()
#            student_mess = u'Данные о студенте - {} - успешно изменены !'.format(student_app.full_name)
            student_mess = u'Данные о студенте - {} {} - успешно изменены !'.format(student_app.name,
                                                                                    student_app.surname)
            messages.success(request, student_mess)
            print 'request.path  = ', request.path
            return redirect(request.path)
    else:
        student_form = StudentForm(instance=student_app)
    return render(request, 'students/edit_student.html', {'student_form': student_form,
                                                          'student_app': student_app}
    )

# Deletion student
def delete_student(request, pk_stud):
    pk_int = int(pk_stud)
    student_app = Student.objects.get(id=pk_int)
    if request.method == 'POST':
        student_app.delete()
#        student_mess = u'Студент - {} - был успешно удален !'.format(student_app.full_name)
        student_mess = u'Студент - {} {} - был успешно удален !'.format(student_app.name,
                                                                        student_app.surname)
        messages.success(request, student_mess)
        return redirect('students:student-list')
    return render(request, 'students/delete_student.html', {'student_app': student_app})

