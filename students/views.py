# -*- coding: utf_8 -*-
from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.contrib import messages
from students.models import Students


class StudentsForm(ModelForm):
    class Meta:
        model = Students


def contact(request):
    return render(request, 'contact.html')


def student_list(request):
    if request.GET:
        n = request.GET[u'course_id']
        stud = Students.objects.filter(course=int(n))
        c = {'stud': stud}
        return render(request, 'student_list.html', c)
    stud = Students.objects.all()
    c = {"stud": stud}
    return render(request, 'student_list.html', c)


def student_detail(request, pk):
    stud = Students.objects.get(id__exact=int(pk))
    c = {"stud": stud}
    return render(request, 'student_detail.html', c)


def student_add(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            student = form.cleaned_data['first_name'] + ' ' + form.cleaned_data['surname']
            messages.success(request, (u'Новый студент %s был добавлен' % student))
            return redirect('student_list')
    else:
        form = StudentsForm()
    context = {'form': form}
    return render(request, 'student_add.html', context)


def student_edit(request, pk):
    student = Students.objects.get(id__exact=int(pk))
    form = StudentsForm(instance=student)
    if request.method == 'POST':
        form = StudentsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            student = form.cleaned_data['first_name'] + ' ' + form.cleaned_data['surname']
            messages.success(request, (u'Информация о студенте %s обновлена' % student))
            return redirect('student_list')
    context = {'form': form}
    return render(request, 'student_edit.html', context)