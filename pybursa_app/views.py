# ~*~ coding: utf-8 ~*~


from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy, reverse
from courses.models import Course, Lesson
from students.models import Student
from coaches.models import Coach
from django.template import RequestContext, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class StudentList(ListView):
    model = Student
    template_name = 'students.html'


class StudentListCourse(ListView):
    model = Student
    def get_queryset(self):
        self.course = Course.objects.get(pk=self.kwargs['course_id'])
        return Student.objects.filter(student_course=self.course)
    def get_context_data(self, **kwargs):
        context = super(StudentListCourse, self).get_context_data(**kwargs)
        context['course_list'] = self.course
        return context

class StudentDetail(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentDetail, self).get_context_data(**kwargs)
        self.student = Student.objects.get(pk=self.kwargs['pk'])
        self.course =  Course.objects.filter(student=self.student)
        context['course_list'] = self.course
        return context

class StudentCreate(CreateView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentCreate, self).get_context_data(**kwargs)
        context['shead'] = 'Введите данные студента'
        context['prompt'] = 'Сохранить данные'
        return context
    def get_success_url(self):
        return reverse('pybursa_app:student_add_redirect', kwargs={'student_id': self.object.pk})

class StudentEdit(UpdateView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentEdit, self).get_context_data(**kwargs)
        self.student = Student.objects.get(pk=self.kwargs['pk'])

        context['shead'] = 'Измените данные студента'
        context['prompt'] = 'Сохранить изменения'
        return context
    def get_success_url(self):
        return reverse('pybursa_app:student_mod_redirect', kwargs={'student_id': self.object.pk})

class StudentDelete(DeleteView):
    model = Student
#    template_name = 'student_delete.html'

    def get_context_data(self, **kwargs):
        context = super(StudentDelete, self).get_context_data(**kwargs)
        self.student = Student.objects.get(pk=self.kwargs['pk'])

        context['shead'] = 'Вы действительно хотите удалить данные студента '
        context['prompt'] = 'Удалить'

        return context
    def get_success_url(self):
        return reverse('pybursa_app:student_list')


class StudentForm(ModelForm):
    class Meta:
        model = Student

class StudentDeleteForm(ModelForm):
    class Meta:
        model = Student
        fields = 'student_name', 'student_last_name', 'student_birth', 'student_email'

def index(request):

    course_list = Course.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'course_list': course_list,
    })
    return HttpResponse(template.render(context))

def contacts(request):
#    return HttpResponse("You're looking at poll %s." % poll_id)
    return render_to_response('contacts.html')

class CourseDetail(DetailView):
    model = Course
    template_name = 'course.html'
    def get_context_data(self, **kwargs):
        context = super(CourseDetail, self).get_context_data(**kwargs)
        self.course = Course.objects.get(pk=self.kwargs['pk'])
        self.lesson =  Lesson.objects.filter(lesson_course=self.course)
        self.student =  Student.objects.filter(student_course=self.course)
        context['lesson_list'] = self.lesson
        context['student_list'] = self.student
        return context

class CourseCreate(CreateView):
    model = Course
    template_name = 'course_add.html'
    def get_context_data(self, **kwargs):
        context = super(CourseCreate, self).get_context_data(**kwargs)
        context['shead'] = 'Введите данные курса'
        context['prompt'] = 'Сохранить данные'
        return context
    def get_success_url(self):
        return reverse('pybursa_app:course_add_redirect', kwargs={'course_id': self.object.pk})


def course(request, course_id):
    course = Course.objects.get(pk=course_id)
    lesson_list = Lesson.objects.filter(lesson_course=course_id)

    template = loader.get_template('course.html')
    context = RequestContext(request, {
        'course': course,
        'lesson_list': lesson_list,
    })

    return HttpResponse(template.render(context))

def coach(request, coach_id):
    coach = Coach.objects.get(pk=coach_id)
    coach_courses = Course.objects.filter(course_coach=coach_id)
    assistant_courses = Course.objects.filter(course_assistent=coach_id)

    template = loader.get_template('coach.html')
    context = RequestContext(request, {
        'coach': coach,
        'coach_courses': coach_courses,
        'assistant_courses': assistant_courses,

    })

    return HttpResponse(template.render(context))





def student_mod_redirect(request, student_id=None):

    student_list = Student.objects.all()
    course_list = Course.objects.all()
    name = ''
    fname = ''
    if student_id:
        s = student_list.get(pk=student_id)
        name= s.student_name
        fname = s.student_last_name

    text = name + u' ' + fname +u"- измененные данные студента записаны в базу данных"
    template = loader.get_template('students.html')
    context = RequestContext(request, {
        'student_list': student_list,
        'course_list': course_list,
        'text': text,
    })

    return HttpResponse(template.render(context))


def student_add_redirect(request, student_id=None):

    student_list = Student.objects.all()
    course_list = Course.objects.all()
    name = ''
    fname = ''
    if student_id:
        s = student_list.get(pk=student_id)
        name= s.student_name
        fname = s.student_last_name

    text = name + u' ' + fname +u"- данные студента добавлены в базу данных"
    template = loader.get_template('students.html')
    context = RequestContext(request, {
        'student_list': student_list,
        'course_list': course_list,
        'text': text,
    })

    return HttpResponse(template.render(context))


def course_add_redirect(request, course_id=None):

    course_list = Course.objects.all()
    name = ''

    if course_id:
        s = course_list.get(pk=course_id)
        name= s.course_name

    text = name + u' ' +u"- данные курса добавлены в базу данных"
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'course_list': course_list,
        'text': text,
    })

    return HttpResponse(template.render(context))
