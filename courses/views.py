# -*- coding: utf_8 -*-
from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from courses.models import Courses, Lesson


class CoursesForm(ModelForm):
    class Meta:
        model = Courses


class LessonForm(ModelForm):
    class Meta:
        model = Lesson


def index(request):
    cour = Courses.objects.all()
    c = {"cour": cour}
    return render(request, 'index.html', c)


class CoursesDetailView(DetailView):
    model = Courses
    template_name = 'course.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(*args, **kwargs)
        context["course"] = self.object
        context["lessons"] = self.object.lesson_set.all()
        return context


class CoursesCreateView(SuccessMessageMixin, CreateView):
    model = Courses
    template_name = 'course_add.html'
    success_url = reverse_lazy('home')
    success_message = u"Новый курс %(name)s был добавлен"


class CoursesUpdateView(SuccessMessageMixin, UpdateView):
    model = Courses
    template_name = 'course_edit.html'
    success_url = reverse_lazy('home')
    success_message = u"Информация о курсе %(name)s обновлена"


class CoursesDeleteView(DeleteView):
    model = Courses
    template_name = 'course_delete.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        response = super(CoursesDeleteView, self).delete(self, request, *args, **kwargs)
        messages.success(request, u"Курс %s был удалён" % self.object.name)
        return response

    def get_context_data(self, *args, **kwargs):
        context = super(CoursesDeleteView, self).get_context_data(*args, **kwargs)
        context["course"] = self.object
        return context


def add_lesson(request, pk):
    course = Courses.objects.get(pk=pk)
    form = LessonForm(initial={'course': course})
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, (u'Занятие %s было добавлено на курс %s' %
                                       (form.cleaned_data['thema'], course.name)))
            return redirect('course', pk)
    context = {'form': form,
               'course': course}
    return render(request, 'add_lesson.html', context)