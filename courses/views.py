# coding=utf-8
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

from courses.models import Course, Lesson
from CourseForm import CourseForm

from CourseLoggingMixin import CourseLoggingMixin


class IndexView(ListView):
    template_name = 'courses/index.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        #logger.debug('Getting courses queryset...')
        return Course.objects.order_by('-id')

class ItemDetailView(CourseLoggingMixin, DetailView):
    model = Course
    template_name = 'courses/detail.html'


def contact(request):
    return render(request, 'courses/contact.html')


class ItemCreateView(SuccessMessageMixin, CreateView):
    model = Course
    template_name = 'courses/add.html'
    success_url = reverse_lazy('courses:index')
    success_message = u"Курс %(title)s успешно добавлен"

    def get_context_data(self, **kwargs):
        context = super(ItemCreateView, self).get_context_data(**kwargs)
        context['action_name'] = "Создать"
        return context


class ItemUpdateView(SuccessMessageMixin, UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    success_url = reverse_lazy('courses:index')
    success_message = u"Данные изменены."
    
    def get_context_data(self, **kwargs):
        context = super(ItemUpdateView, self).get_context_data(**kwargs)
        context['action_name'] = "Изменить"
        return context


class ItemDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('courses:index')
    
    def get_context_data(self, **kwargs):
        context = super(ItemDeleteView, self).get_context_data(**kwargs)
        context['action_name'] = "Удалить"
        return context

    def delete(self, request, *args, **kwargs):
        success_message = u"Курс " + self.get_object().title + u" был удален."
        messages.success(self.request, success_message)
        return super(ItemDeleteView, self).delete(request, *args, **kwargs)


