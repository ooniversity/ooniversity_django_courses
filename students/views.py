# coding=utf-8
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

from students.models import Student
#from StudentForm import StudentForm


class ItemListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        pk = self.request.GET.get('course_id', None)
        if pk:
            linked_students = Student.objects.filter(courses=int(pk))
        else:
            linked_students = Student.objects.all()

        return linked_students


class ItemDetailView(DetailView):
    model = Student


class ItemCreateView(SuccessMessageMixin, CreateView):
    model = Student
    success_url = reverse_lazy('students:index')
    success_message = u"Студент %(name)s %(surname)s успешно добавлен"

    def get_context_data(self, **kwargs):
        context = super(ItemCreateView, self).get_context_data(**kwargs)
        context['action_name'] = "Создать"
        context['action_text'] = "Создание нового студента"
        return context


class ItemUpdateView(SuccessMessageMixin, UpdateView):
    model = Student
    success_message = u"Данные изменены."
    
    def get_context_data(self, **kwargs):
        context = super(ItemUpdateView, self).get_context_data(**kwargs)
        context['action_name'] = "Изменить"
        context['action_text'] = "Редактирование данных студента"
        return context


class ItemDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:index')
    
    def get_context_data(self, **kwargs):
        context = super(ItemDeleteView, self).get_context_data(**kwargs)
        context['action_name'] = "Удалить"
        return context

    def delete(self, request, *args, **kwargs):
        success_message = u"Студент " + self.get_object().full_name() + u" был удален."
        messages.success(self.request, success_message)
        return super(ItemDeleteView, self).delete(request, *args, **kwargs)

