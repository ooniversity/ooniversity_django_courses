# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from students.models import Student
from django import forms
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


#Создаем форму для веб браузера на основе модели Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        #Указываем поля, которые не нужно выводить пользователю


# С помощью класса DetailView выводим информацию о студенте на HTML страничку
class StudentDetailView(DetailView):
    model = Student


# С помощью класса ListView выводим список студентов на HTML страничку
class StudentListView(ListView):
    model = Student
    paginate_by = 2

    #Определяем какую выборку данных показывать - или всех студентов, или студентов конкретного курса
    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id is None:
            student_list = Student.objects.all()
        else:
            student_list = Student.objects.filter(courses__id = course_id)
        return student_list


#Класс для создания студента
class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:student-list')

    def form_valid(self, form):
        self.application = form.save()
        messages.success(self.request, u'Студент {} {} успешно добавлен'.format(self.application.surname, self.application.name))
        return super(StudentCreateView, self).form_valid(form)

    #Добавляем название страницы шаблона HTML в контекстные данные
    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['page_title'] = u"Создание студента"
        return context


#Класс для редактирования(обновления) данных студента
class StudentUpdateView(UpdateView):
    model = Student

    def get_success_url(self):
        return reverse_lazy('students:edit-student', kwargs={'pk':self.kwargs['pk']})

    def form_valid(self, form):
        self.application = form.save()
        messages.success(self.request, u'Данные студента {} {} изменены'.format(self.application.surname, self.application.name))
        return super(StudentUpdateView, self).form_valid(form)

    #Добавляем название страницы шаблона HTML в контекстные данные
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = u"Редактирование студента"
        return context


#Класс для удаления данных студента
class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:student-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, u'Запись успешно удалена')
        return super (StudentDeleteView, self).delete(request, *args, **kwargs)



#Вьюшка для создания студента
#def create_student(request):
#    if request.method == 'POST':
#        #Инстанцирование формы для студента
#        model_form = StudentForm(request.POST)
#        if model_form.is_valid():
#            application = model_form.save()
#            messages.success(request, u'Студент {} {} успешно добавлен'.format(application.surname, application.name))
#            return redirect ('students:student-list')
#    else:
#        model_form = StudentForm()
#    return render(request, 'students/new_student.HTML',
#                  {'model_form':model_form})


#Вьюшка для редактирования данных студента
#def edit_student(request, pk):
#    application = Student.objects.get(id=pk)
#    if request.method == 'POST':
#        model_form = StudentForm(request.POST, instance=application)
#        if model_form.is_valid():
#            application = model_form.save()
#            messages.success(request, u'Данные студента {} {} успешно изменены'.format(application.surname, application.name))
#            return redirect (request.path)
#    else:
#        model_form = StudentForm(instance=application)
#    return render(request, 'students/edit_data_student.HTML',
#                  {'model_form':model_form})



#Вьюшка для удаления студента
#def remove_student(request, pk):
#    application = Student.objects.get(id=pk)
#    if request.method == 'POST':
#        application.delete()
#        messages.success(request, u'Студент {} {} был удален'.format(application.surname, application.name))
#        return redirect ('students:student-list')
#    return render(request, 'students/remove_student.HTML',
#                  {'student':application})
