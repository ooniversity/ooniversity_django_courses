# -*- coding: utf-8 -*-

#from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from students.models import Student
from students.forms import StudentModelForm


class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        course_id = self.request.GET.get('course_id')
        if course_id != None:
            #course_id = int(course_id)
            student_list = Student.objects.filter(courses__id=course_id)
        else:
            student_list = Student.objects.all()
        return student_list


class StudentDetailView(DetailView):
    model = Student



# Class-based Views for forms edition student:

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:student-list')

    def form_valid(self, form):
        self.student = form.save()
        message = u'Студент - {} {} - успешно добавлен !'.format(self.student.name,
                                                                 self.student.surname)
        messages.success(self.request, message)
        return super(StudentCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['block_title'] = u'Ooniversity - New student'
        context['page_title'] = u'Добавление нового студента'
        return context


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm

    def get_success_url(self):
        #print 'self.request.path  = ', self.request.path
        return reverse_lazy('students:student-edit', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.student = form.save()
        message = u'Данные о студенте - {} {} - успешно изменены !'.format(self.student.name,
                                                                           self.student.surname)
        messages.success(self.request, message)
        return super(StudentUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['block_title'] = u'Edition Student'
        context['page_title'] = u'Редактирование данных студента - '
        return context


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:student-list')

    def delete(self, request, *args, **kwargs):
        student = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        message = u'Студент - {} {} - был успешно удален !'.format(self.object.name,
                                                                   self.object.surname)
        messages.success(self.request, message)
        return student



"""

def students(request):
    if request.GET.get('course_id') != None:
        course_id = int(request.GET.get('course_id'))
        students = Student.objects.filter(courses__id=course_id)
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
            return redirect('students:student-edit', pk_stud)
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

"""
