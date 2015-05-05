# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm

import logging
logger = logging.getLogger(__name__)

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_coaches.html'
    context_object_name = 'course'
    pk_url_kwarg = 'id_course'
    
    def get_context_data(self, *args, **kwargs):

        logger.debug(u'Отладочная информация')
        logger.info(u'Информационное сообщение')
        logger.warning(u'Предупреждающая информация')
        logger.error(u'Информация об ошибке')

        context = super(CourseDetailView, self).get_context_data(*args, **kwargs)
        self.course = Course.objects.get(pk=self.kwargs['id_course'])
        context['course'] = self.course
        context["lessons"] = self.course.lesson_set.all()
        return context

# Class-based Views for forms edition course:
class CourseCreateView(CreateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/add_course.html'
    success_url = reverse_lazy('index-ooniversity')
        
    def form_valid(self, form):
        form.save()
        message = u'Курс - {} - успешно добавлен !'.format(self.course.title)
        messages.success(self.request, message)
        return super(CourseCreateView, self).form_valid(form)

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/edit_course.html'
    context_object_name = 'course_app'
    pk_url_kwarg = 'pk_course'
    def get_success_url(self):
        return reverse_lazy('courses:edit-course',
            kwargs={'pk_course': self.object.pk}
        )
    def form_valid(self, form):
        form.save()
        message = u'Данные о курсе - {} - успешно изменены !'.format(self.course.title)
        messages.success(self.request, message)
        return super(CourseUpdateView, self).form_valid(form)

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/delete_course.html'
    context_object_name = 'course_app'
    pk_url_kwarg = 'pk_course'
    success_url = reverse_lazy('index-ooniversity')
    def delete(self, request, *args, **kwargs):
        course = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        message = u'Курс - {} - был успешно удален !'.format(self.object.title)
        messages.success(self.request, message)
        return course
# View for form - Creation new lesson:
def add_lesson(request, pk_course):
    pk_int = int(pk_course)
    lesson_course = Course.objects.get(id=pk_int)
    if request.method == 'POST':
        lesson_form = LessonModelForm(request.POST, initial={'course': lesson_course})
        if lesson_form.is_valid():
            lesson_app = lesson_form.save()
            lesson_mess = u'Занятие - {} - было успешно создано !'.format(lesson_app.theme)
            messages.success(request, lesson_mess)
            return redirect('courses:course-coaches', pk_course)
    else:
        lesson_form = LessonModelForm(initial={'course': lesson_course})
    return render(request, 'courses/add_lesson.html', {'lesson_form': lesson_form,
                                                                                'lesson_course': lesson_course}
    )












