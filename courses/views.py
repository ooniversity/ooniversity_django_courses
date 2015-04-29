# ~*~ coding: utf-8 ~*~


from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy, reverse
from courses.models import Course, Lesson
from students.models import Student
from coaches.models import Coach
from django.template import RequestContext, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django import forms
from django.forms import ModelForm

import logging
logger = logging.getLogger(__name__)
logger.debug(u'Точка входа в  %s (редактирование и удаление)', __name__)
logger.info(u'Точка входа в %s', __name__)
logger.warning(u'Точка входа в %s', __name__)
logger.error(u'Точка входа в %s', __name__)
logger.critical(u'Точка входа в %s', __name__)


class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = 'lesson_number', 'lesson_course', 'lesson_theme', 'lesson_description'

class CourseEdit(UpdateView):
    model = Course
    form_class = LessonForm
    template_name = 'course_add.html'

    def get_context_data(self, **kwargs):
        context = super(CourseEdit, self).get_context_data(**kwargs)
        self.course = Course.objects.get(pk=self.kwargs['pk'])

        context['shead'] = 'Измените данные курса'
        context['prompt'] = 'Сохранить изменения'
        return context
    def get_success_url(self):
        return reverse('courses:course_mod_redirect', kwargs={'course_id': self.object.pk})

class CourseDelete(DeleteView):
    model = Course
    template_name = 'course_delete.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDelete, self).get_context_data(**kwargs)
        self.course = Course.objects.get(pk=self.kwargs['pk'])

        context['shead'] = 'Вы действительно хотите удалить данные курса '
        context['prompt'] = 'Удалить'

        return context
    def get_success_url(self):
        return reverse('pybursa_app:index')



def lesson_add(request, course_id):


    if request.method == 'POST':

        form = LessonForm(request.POST)
        if form.is_valid():
            new = form.save()

            lesson_id = new.id

            return HttpResponseRedirect('/lesson/add/%s/' % lesson_id)
    else:
        c = Lesson.objects.filter(lesson_course=course_id)
        num = 0
        if c:
            cc = c.order_by('-lesson_number')[0]
            num = cc.lesson_number

        num += 1
        form = LessonForm(initial={'lesson_number': num,'lesson_course': course_id})

    c = Course.objects.get(pk=course_id)
    text = u"Введите тему занятия номер "+ unicode(num) +u" для курса "+ c.course_name
    course = course_id
    prompt = "Сохранить данные"
    template = loader.get_template('lesson_add.html')
    context = RequestContext(request, {'form': form, 'shead': text, 'prompt': prompt, "course": course, "number": num})

    return HttpResponse(template.render(context))

def lesson_add_redirect(request, lesson_id):


    s = Lesson.objects.get(pk=lesson_id)
    course_id = s.lesson_course.id

    course = Course.objects.get(pk=course_id)
    lesson_list = Lesson.objects.filter(lesson_course=course_id)
    name= s.lesson_theme

    text = name +u": данные по теме добавлены в базу данных"
    template = loader.get_template('course.html')
    context = RequestContext(request, {
        'lesson_list': lesson_list,
        'course': course,
        'text': text,
    })

    return HttpResponse(template.render(context))


def lesson_mod(request, lesson_id = None):
    s = Lesson.objects.get(pk=lesson_id)
    course_id = s.lesson_course.id
    form = LessonForm(instance=s)
    if request.method == 'POST':

        form = LessonForm(request.POST, instance=s)

        if form.is_valid():
            st = form.save()

            return HttpResponseRedirect('/lesson/mod/%s/%s/' % (course_id, lesson_id))


    text = u"Измените данные темы номер "+ unicode(s.lesson_number)
    prompt = "Сохранить изменения"
    template = loader.get_template('lesson_add.html')
    context = RequestContext(request, {'form': form, 'shead': text, 'prompt':prompt,"course": course_id})
    return HttpResponse(template.render(context))


def lesson_rem(request, lesson_id = None):
    lesson = Lesson.objects.get(pk=lesson_id)
    course_id = lesson.lesson_course.id
    form = LessonForm(instance=lesson)
    if request.method == 'POST':
        d = lesson.delete()
        return HttpResponseRedirect('/course/%s/' % course_id)

    text = "Удалить данные по теме?"
    prompt = "Удалить"
    template = loader.get_template('lesson_add.html')
    context = RequestContext(request, {'form': form, 'shead': text, 'prompt':prompt, "course": course_id})
    return HttpResponse(template.render(context))

def lesson_mod_redirect(request, course_id, lesson_id):
    course = Course.objects.get(pk=course_id)
    lesson_list = Lesson.objects.filter(lesson_course=course_id)

    template = loader.get_template('course.html')


    s = lesson_list.get(pk=lesson_id)
    name= s.lesson_theme

    text = name + u": измененные данные занятия записаны в базу данных"
    template = loader.get_template('course.html')
    context = RequestContext(request, {
        'lesson_list': lesson_list,
        'course': course,
        'text': text,
    })

    return HttpResponse(template.render(context))


def course_mod_redirect(request, course_id=None):

    course_list = Course.objects.all()
    name = ''

    if course_id:
        s = course_list.get(pk=course_id)
        name= s.course_name

    text = name + u' ' +u"- данные курса изменены в базе данных"
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'course_list': course_list,
        'text': text,
    })

    return HttpResponse(template.render(context))
