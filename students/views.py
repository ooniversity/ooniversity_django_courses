# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from students.models import Student
from django import forms
from django.contrib import messages


#Создаем форму для веб браузера на основе модели Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        #Указываем поля, которые не нужно выводить пользователю


#Вьюшка для создания студента
def create_student(request):
    if request.method == 'POST':
        #Инстанцирование формы для студента
        model_form = StudentForm(request.POST)
        if model_form.is_valid():
            application = model_form.save()
            messages.success(request, u'Студент {} {} успешно добавлен'.format(application.surname, application.name))
            return redirect ('students:student_list')
    else:
        model_form = StudentForm()

    return render(request, 'students/new_student.HTML',
                  {'model_form':model_form})

#
def show_students(request):
    if request.GET.get('course_id') is None:
        students = Student.objects.all()
        return render(request, 'students/student_list.HTML',
                      {'students': students})
    else:
        students = Student.objects.filter(courses__id = \
                                          int(request.GET.get('course_id')))
        return render(request, 'students/student_list.HTML',
                      {'students': students})


def show_student_detail(request, id):
    id_course=int(id)
    student = Student.objects.get(id = id_course)
    return render(request, 'students/students.HTML', {'student': student})
