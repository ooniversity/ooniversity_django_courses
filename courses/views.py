# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import Http404
from courses.models import Course, Lesson, Comment, MailCourse
from django import forms
from django.contrib import messages
from django.contrib import auth
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
import logging
logger = logging.getLogger(__name__) #courses.view

#Создаем форму для веб браузера на основе модели Course
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        #Указываем поля, которые не нужно выводить пользователю


#Создаем форму для веб браузера на основе модели Course
class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        #Указываем поля, которые не нужно выводить пользователю


# С помощью класса DetailView выводим информацию о курсе на HTML страничку
class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/courses.HTML'
    context_object_name = 'course'
    #Переопределяем context
    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        course = Course.objects.get(pk = self.kwargs['pk'])
        print len(course.student_set.all())
        #логгирование
        logger.debug(u'Some debug info for course - {}'.format(course.name))
        logger.info(u'Some info discription for course - {}'.format(course.name))
        logger.warning(u'Some warning info for course - {}'.format(course.name))
        logger.error(u'Some error info for course - {}'.format(course.name))
        context['course'] = course
        courses = Course.objects.all()
        context['courses'] = courses
        context['username'] = auth.get_user(self.request).username
        return context


#Класс для создания курса
class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/new_course.HTML'
    context_object_name = 'course'
    success_url = ('/')

    def form_valid(self, form):
        self.application = form.save()
        messages.success(self.request, u'Курс {} успешно добавлен'.format(self.application.name))
        return super(CourseCreateView, self).form_valid(form)




#Класс для редактирования(обновления) данных о курсе
class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit_data_course.HTML'
    context_object_name = 'course'

    def get_success_url(self):
        return reverse_lazy('courses:edit-course', kwargs={'pk':self.kwargs['pk']})

    def form_valid(self, form):
        self.application = form.save()
        messages.success(self.request, u'Данные о курсе {} изменены'.format(self.application.name))
        return super(CourseUpdateView, self).form_valid(form)


#Класс для удаления данных о курсе
class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove_course.HTML'
    context_object_name = 'course'
    success_url = reverse_lazy('index_itbursa')

    def delete(self, request, *args, **kwargs):
        course = super (CourseDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, u'Курс {} успешно удален'.format(self.object.name))
        return course


#Вьюшка для создания нового урока
def create_lesson(request, pk):
    if request.method == 'POST':
        #Инстанцирование формы для урока
        model_form = LessonForm(request.POST)
        if model_form.is_valid():
            application = model_form.save()
            messages.success(request, u'Урок {} для курса {} успешно добавлен'.format(application.theme, application.course.name))

            return redirect ('courses:course', application.course_id)
    else:
        model_form = LessonForm(initial={'course':pk,})
    return render(request, 'courses/new_lesson.HTML',
                  {'model_form':model_form})


#Вьюшка для редактирования нового урока
def edit_lesson(request, pk):
    application = Course.objects.get(id=pk)
    if request.method == 'POST':
        model_form = LessonForm(request.POST, instance=application)
        if model_form.is_valid():
            application = model_form.save()
            messages.success(request, u'Данные {} для урока {} изменены'.format(application.theme,
                                                                                application.course.name))
            return redirect (request.path)
    else:
        model_form = LessonForm(instance=application)
    return render(request, 'courses/edit_data_lesson.HTML',
                  {'model_form':model_form})



#Класс для создания коментария курса
class CommentCreateView(CreateView):
    model = Comment
    template_name = 'courses/new_comment.HTML'
    context_object_name = 'comment'

    def get_initial(self):
         return {'course': self.kwargs['pk'],
                'autor': auth.get_user(self.request).username}

    def get_success_url(self):
        return reverse_lazy('courses:course', kwargs={'pk':self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        courses = Course.objects.all()
        context['courses'] = courses
        context['username'] = auth.get_user(self.request).username
        return context

    def form_valid(self, form):
        self.application = form.save()
        messages.success(self.request, u'Ваш отзыв успешно добавлен')
        return super(CommentCreateView, self).form_valid(form)


#Класс для редактирования коментариев о курсе
class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'courses/edit_data_comment.HTML'
    context_object_name = 'comment'

    def get_success_url(self):
        return reverse_lazy('courses:course', kwargs={'pk':int(self.kwargs['id'])})

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        courses = Course.objects.all()
        context['courses'] = courses
        context['username'] = auth.get_user(self.request).username
        return context

    def form_valid(self, form):
        self.application = form.save()
        messages.success(self.request, u'Отзыв успешно изменен')
        return super(CommentUpdateView, self).form_valid(form)


#Класс для удаления комментария о курсе
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'courses/remove_comment.HTML'
    context_object_name = 'comment'
    #success_url = reverse_lazy('index_itbursa')

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        courses = Course.objects.all()
        context['courses'] = courses
        context['username'] = auth.get_user(self.request).username
        return context

    def get_success_url(self):
        return reverse_lazy('courses:course', kwargs={'pk':int(self.kwargs['id'])})

    def delete(self, request, *args, **kwargs):
        comment = super (CommentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, u'Отзыв успешно удален')
        return comment

#Отправка заявок студентов на выбранный курс обучения
class MailCourseCreateView(CreateView):
    template_name = 'courses/enroll.html'
    model = MailCourse
    success_url = '/'

    def get_initial(self):
        return {'course': self.kwargs['pk'],}

    def get_context_data(self, **kwargs):
        context = super(MailCourseCreateView, self).get_context_data(**kwargs)
        courses = Course.objects.all()
        context['courses'] = courses
        context['username'] = auth.get_user(self.request).username
        return context

    def form_valid(self, form):
        self.application = form.save()
        address_list = [address for (login, address) in settings.ADMINS]
        send_mail(
            subject='Запись на курс {}'.format(self.application.course),
            message=u'Студент {} {} записался на курс {}. Телефон - {}. Email - {}'.format(self.application.surname,
                                                                                           self.application.name,
                                                                                           self.application.course,
                                                                                           self.application.phone,
                                                                                           self.application.email,),
            from_email=self.application.email,
            recipient_list=address_list,
        )
        messages.success(self.request, u'Ваша заявка отправлена. Ожидайте, мы с Вами свяжемся. Спасибо, что выбрали нас!')

        return super(MailCourseCreateView, self).form_valid(form)

#qs = Lesson.objects.get(id=pk)
#Вьюшка для удаления урока
#def remove_lesson(request, pk):
#    application = Lesson.objects.get(id=pk)
#    if request.method == 'POST':
#        application.delete()
#        messages.success(request, u'Урок {} был удален'.format(application.theme))
#        return redirect (request.path[:request.path.find(pk)+1])
#    return render(request, 'courses/remove_course.HTML',
#                  {'course':application})
