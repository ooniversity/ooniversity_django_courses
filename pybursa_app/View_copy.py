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
#    template_name = 'student_list.html'
    def get_queryset(self):
        self.course = Course.objects.get(pk=self.kwargs['course_id'])
        return Student.objects.filter(student_course=self.course)
    def get_context_data(self, **kwargs):
        context = super(StudentListCourse, self).get_context_data(**kwargs)
        context['course_list'] = self.course
        return context

class StudentDetail(DetailView):
    model = Student
    context_object_name = 'student_list'
    def get_context_data(self, **kwargs):
        context = super(StudentDetail, self).get_context_data(**kwargs)
        self.student = Student.objects.get(pk=self.kwargs['pk'])
        self.course =  Course.objects.filter(student=self.student)
        context['course_list'] = self.course
        return context

class StudentCreate(CreateView):
    model = Student
    template_name = 'student_add.html'
#    success_url = reverse_lazy('pybursa_app:student_add_redirect')
#                                 kwargs={'student_id':model.id})
    def get_context_data(self, **kwargs):
        context = super(StudentCreate, self).get_context_data(**kwargs)
        context['shead'] = 'Введите данные студента'
        context['prompt'] = 'Сохранить данные'
        return context
    def get_success_url(self):
        return reverse('pybursa_app:student_add_redirect', kwargs={'student_id': self.object.pk})

class StudentEdit(UpdateView):
    model = Student
    template_name = 'student_add.html'

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
    template_name = 'student_delete.html'

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


#    return render_to_response('index.html')

def contacts(request):
#    return HttpResponse("You're looking at poll %s." % poll_id)
    return render_to_response('contacts.html')

def student_list(request, course_id=None):
    if course_id:
        student_list = Student.objects.filter(student_course=course_id)
        course_list = Course.objects.get(pk=course_id)
        template = loader.get_template('student_list.html')
    else:
        student_list = Student.objects.all()
        course_list = Course.objects.all()
        template = loader.get_template('students.html')

    context = RequestContext(request, {
        'student_list': student_list,
        'course_list': course_list,
    })

    return HttpResponse(template.render(context))

def students(request):

    student_list = Student.objects.all()
    course_list = Course.objects.all()

    template = loader.get_template('students.html')
    context = RequestContext(request, {
        'student_list': student_list,
        'course_list': course_list,
    })

    return HttpResponse(template.render(context))

def student_detail(request, student_id):
    student_list = Student.objects.get(pk=student_id)
    course_list = Course.objects.filter(student=student_id)
    template = loader.get_template('student_detail.html')
    context = RequestContext(request, {
        'student_list': student_list,
        'course_list': course_list,
    })
    return HttpResponse(template.render(context))

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

def student_add(request):


    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():

            new_student = form.save()
            student_id = new_student.id
            return HttpResponseRedirect('/student/add/%s/' % student_id)

    else:
        form = StudentForm()
    text = "Введите данные студента:"
    prompt = "Сохранить данные"
    template = loader.get_template('student_add.html')
    context = RequestContext(request, {'form': form, 'shead': text, 'prompt':prompt})
    return HttpResponse(template.render(context))



def student_mod(request, student_id = None):
    student = Student.objects.get(pk=student_id)
    form = StudentForm(instance=student)
    if request.method == 'POST':

        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            st = form.save()

            return HttpResponseRedirect('/student/mod/%s/' % student_id)


    text = "Измените данные студента:"
    prompt = "Сохранить изменения"
    template = loader.get_template('student_add.html')
    context = RequestContext(request, {'form': form, 'shead': text, 'prompt':prompt})
    return HttpResponse(template.render(context))


def student_rem(request, student_id = None):
    student = Student.objects.get(pk=student_id)
    form = StudentDeleteForm(instance=student)
    if request.method == 'POST':
        d = student.delete()
        return HttpResponseRedirect('/student_list/')

    text = "Удалить данные студента?"
    prompt = "Удалить"
    template = loader.get_template('student_add.html')
    context = RequestContext(request, {'form': form, 'shead': text, 'prompt':prompt})
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
