from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import Course, Lesson
from django import forms
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course.html"


class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index_pybursa')
    template_name = "courses/add_course.html"

    def form_valid(self, form):
        super_valid = super(CourseCreateView, self).form_valid(form)
        msg = "Course {} was added!".format(self.object.name)
        messages.success(self.request, msg)
        return super_valid


class CourseUpdateView(UpdateView):
    model = Course
    success_url = reverse_lazy('index_pybursa')
    template_name = "courses/edit_course.html"

    def form_valid(self, form):
        msg = "Course edited!"
        messages.success(self.request, msg)
        return super(CourseUpdateView, self).form_valid(form) 


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index_pybursa')
    template_name = "courses/delete_course.html"

    def delete(self, request, *args, **kwargs):
        delete_super = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request,
                         u'Course {} deleted.'.format(self.object.name))
        return delete_super


def add_lesson(request, id):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            application = form.save()
            msg = "Lesson {} was added!".format(application.theme)
            messages.success(request, msg)
            return redirect('courses:course', application.course.id)
    else:
        form = LessonForm(initial={'course': id})
    return render(request, 'courses/add_lesson.html', {'form': form})

