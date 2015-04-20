# -*- coding: utf-8 -*-

from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from students.models import Student


class StudentsListView(ListView):
    model = Student

    def get_queryset(self):
        course_id = self.request.GET.get('course_id')
        if course_id:
            students = Student.objects.filter(courses=course_id)
        else:
            students = Student.objects.all()
        return students


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:student_list')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['page_title'] = u"Создание нового студента"
        return context
    
    def form_valid(self, form):
        form = super(StudentCreateView, self).form_valid(form)
        messages.success(self.request, 
                 u"Студент {0} успешно добавлен"\
                  .format(self.object.full_name()))
        return form


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

'''
def student_add(request):
    page_title = u"Создание нового студента"
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = Student()
            new_student = form.save()
            messages.success(request, 
                             u"Студент {0} успешно добавлен"\
                              .format(new_student.full_name()))
            return redirect('students:student_list')
        else:
            return render(request, 'add_edit.html', {'form': form, 'page_title':page_title})
    else:
        form = StudentForm()   
    return render(request, 'add_edit.html', {'form': form, 'page_title':page_title})
'''

def student_edit(request, student_id):
    page_title = u"Редактирование данных студента"
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, 
                            u"Изменения данных студента сохранены в {0}"\
                             .format(datetime.now().strftime("%H:%M:%S")))
            return redirect('students:student_edit', student_id)
        else:
            return render(request, 
                          'add_edit.html', {'form': form, 'page_title':page_title})
    else:
        form = StudentForm(instance=student)   
    return render(request, 'add_edit.html', {'form': form, 'page_title':page_title})


def student_remove(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    full_name = student.full_name()
    page_title = u"Удаление студента"
    page_header = u"Студент {0} будет удалён".format(full_name)
    if request.method == 'POST':
        student.delete()
        messages.success(request,u"Студент {0} был удалён"\
                         .format(full_name))
        return redirect('students:student_list')
    return render(request, 'remove.html', {'student': student, 'page_title':page_title, 'page_header':page_header})

