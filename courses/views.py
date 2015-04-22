# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from django import forms
from django.contrib import messages


from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'


def index_courses(request):
    courses = Course.objects.get()
    return render(request, 'index_courses.html', {'courses': courses})


def course_description(request, course_id):
    course = Course.objects.get(pk=course_id)
    lessons = Lesson.objects.filter(course=course).order_by('number')
    return render(request, 'course_detail.html', {'course': course, 'lessons': lessons})


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            new_course = form.save()
            messages.success(request, 'Course %s successfully added' % new_course.name)
            return redirect('home')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})


def edit_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, "Course data %s was successfully changed" % course.name)
            return redirect('home')
    else:
        form = CourseForm(instance=course)
    return render(request, 'edit_course.html', {'form': form})


def delete_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.method == "POST":
        course.delete()
        messages.success(request, "Course %s was successfully deleted" % course.name)
        return redirect('home')
    return render(request, 'delete_course.html', {'course': course})


def add_lesson(request, course_id):
    if request.POST:
        form = LessonForm(request.POST)
        if form.is_valid():
            new_lesson = form.save()
            messages.success(request, "Lesson %s successfully added" % new_lesson.theme)
            return redirect('courses:course_description', course_id)
    else:
        course = Course.objects.get(pk=course_id)
        form = LessonForm(initial={'course':course})
    return render(request, 'add_lesson.html', {'form': form})


#create DetailView, CrateView, UpdateView, DeleteView views
#createe DetailView
class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
    #context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        course = self.get_object()
        print self.kwargs['pk']
        print 1
        context['lessons'] = course.lesson_set.all()
        return context


#create CreateView - view for create Course
class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    context_object_name = 'course'
    template_name = 'add_course.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super(CourseCreateView, self).form_valid(form)
        messages.success(self.request, 'Course %s successfully added' % self.object.name)
        return response


#create UpdateView - view for update Course
class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    context_object_name = 'course'
    template_name = 'edit_course.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super(CourseUpdateView, self).form_valid(form)
        messages.success(self.request, 'Data courses %s was successfully changed' % self.object.name)
        return response


#create DeleteView - view for delete Course
class CourseDeleteView(DeleteView):
    model = Course
    context_object_name = 'course'
    template_name = 'delete_course.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        response = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        messages.warning(request, "Course %s was successfully deleted" % self.object.name)
        return response