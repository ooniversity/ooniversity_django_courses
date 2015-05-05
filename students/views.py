# -*- coding: utf_8 -*-
import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from students.models import Students

logger = logging.getLogger(__name__)


def contact(request):
    return render(request, 'contact.html')


class StudentsListView(ListView):
    logger.debug('it works')
    model = Students
    template_name = 'students/students_list.html'
    paginate_by = 2

    def get_queryset(self):
        logger.debug('it works')
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Students.objects.filter(course=course_id)
            if not students:
                logger.warning('course_id is out of range, no students with course_id=%s' % course_id)
            else:
                logger.info('Student list was created with course_id=%s' % course_id)
        else:
            students = Students.objects.all()
            logger.info('Student list was created without course_id')
        return students


class StudentsDetailView(DetailView):
    logger.debug('it works')
    model = Students


class StudentsCreateView(SuccessMessageMixin, CreateView):
    logger.debug('it works')
    model = Students
    success_url = reverse_lazy('student_list')
    success_message = u"Студент %(first_name)s %(surname)s был успешно создан"


class StudentsUpdateView(SuccessMessageMixin, UpdateView):
    logger.debug('it works')
    model = Students
    success_url = reverse_lazy('student_list')
    template_name_suffix = '_update_form'
    success_message = u"Информация о студенте %(first_name)s %(surname)s была успешно обновлена"


class StudentsDeleteView(DeleteView):
    logger.debug('it works')
    model = Students
    success_url = reverse_lazy('student_list')

    def delete(self, request, *args, **kwargs):
        response = super(StudentsDeleteView, self).delete(self, request, *args, **kwargs)
        student = self.object.first_name + ' ' + self.object.surname
        messages.success(request, u"Студент %s был удалён" % student)
        logger.error('Student %s was deleted' % student)
        return response