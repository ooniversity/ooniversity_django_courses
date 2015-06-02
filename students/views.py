# -*- coding: utf-8 -*-
import logging

from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.contrib import messages
from django.contrib import auth
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils.datastructures import MultiValueDictKeyError

from students.models import Student
from courses.models import Course

logger = logging.getLogger(__name__) #courses.view


#Создаем форму для веб браузера на основе модели Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        #Указываем поля, которые не нужно выводить пользователю


# С помощью класса DetailView выводим информацию о студенте на HTML страничку
class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        student = get_object_or_404(Student, pk = self.kwargs['pk'])
        #логгирование
        logger.debug(u'Some debug info for student - {} {}'.format(student.name, student.surname))
        logger.info(u'Some info discription for student - {} {}'.format(student.name, student.surname))
        logger.warning(u'Some warning info for student - {} {}'.format(student.name, student.surname))
        logger.error(u'Some error info for student - {} {}'.format(student.name, student.surname))
        context['student'] = student
        courses = Course.objects.all()
        context['courses'] = courses
        context['username'] = auth.get_user(self.request).username
        return context


# С помощью класса ListView выводим список студентов на HTML страничку
class StudentListView(ListView):
    model = Student
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        courses = Course.objects.all()
        context['courses'] = courses
        context['username'] = auth.get_user(self.request).username
        return context

    #Определяем какую выборку данных показывать - или всех студентов, или студентов конкретного курса
    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id is None:
            student_list = Student.objects.all()
            #student_list = Student.objects.filter(gender = 'W')
            if len(self.request.GET) and not(len(dict(self.request.GET))==1 and dict(self.request.GET).has_key('page')):
                print dict(self.request.GET),len(dict(self.request.GET)), 'Hello!'
                get_param_list = []
                sum_get_param = 0
                for param in ['Man', 'Woman'] + [str(course.id) for course in Course.objects.all()]:
                    try:
                        if self.request.GET[param]:
                            get_param_list.append(param)
                            sum_get_param += 1
                    except MultiValueDictKeyError:
                        print 'Parameter {} not defined'.format(param)
                    if sum_get_param == len(self.request.GET):
                        break
                index = 1000
                for i in get_param_list:
                    if i == 'Man' or i == 'Woman':
                        index = get_param_list.index(i)
                #print index
                #print get_param_list
                #Фильтрация данных, где выбраны только курсы
                if index == 1000:
                    student_list = Student.objects.filter(courses__id__in = get_param_list)
                #Фильтрация только половых данных
                if index == 0 and (len(get_param_list)<2):
                    student_list = Student.objects.filter(gender = str(get_param_list[0][:1]))
                #Фильтрование и половых данных, и данных курса
                if index == 0 and (len(get_param_list)>=2):
                    student_list = Student.objects.filter(gender = str(get_param_list[0][:1])).filter(courses__id__in = get_param_list[1:])
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
        context['username'] = auth.get_user(self.request).username
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
        context['username'] = auth.get_user(self.request).username
        return context


#Класс для удаления данных студента
class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:student-list')

    def delete(self, request, *args, **kwargs):
        student = super (StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, u'Запись о студенте {} {} успешно удалена'.format(self.object.surname, self.object.name))
        return student



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
