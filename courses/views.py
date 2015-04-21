from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404

from courses.models import Course, Lesson, CourseForm, LessonForm

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def index_courses(request):
    courses = Course.objects.all()

    return render(request, 'courses/index_courses.html', {'courses': courses})


class CourseDetailView(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        course = self.get_object()
        context['course_lessons'] = (
            course.lessons_list.all().order_by('num_in_plan'))
        return context


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('home')
    template_name = "courses/course_delete.html"
    success_message = "Course: '%(title)s' was deleted success!"

    def delete(self, request, *args, **kwargs):
        course = self.get_object()
        messages.success(self.request, self.success_message % {
            'title': course.title,
        })
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)


class CourseCreateView(SuccessMessageMixin, CreateView):
    model = Course
    success_url = reverse_lazy('home')
    template_name = "courses/course_add.html"
    success_message = "Course: '%(title)s' was added success!"


class CourseUpdateView(SuccessMessageMixin, UpdateView):
    model = Course
    success_url = reverse_lazy('home')
    template_name = "courses/course_edit.html"
    success_message = "Course: '%(title)s' was updated success!"


def lesson_add(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(
                request, u"Lesson: {} add success!".format(
                    lesson.theme))
            return redirect('courses:show', course_id)
    else:
        form = LessonForm(initial={'course': course})

    return render(request, 'courses/lesson_add.html', {
        'form': form,
        'course': course,
    })


def lesson_edit(request, pk):
    lesson = Lesson.objects.get(id=pk)
    course = lesson.course

    if request.method == "POST":
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            lesson.save()
            messages.success(
                request, u"Lesson: {} update success!".format(
                    lesson.theme))
            return redirect('courses:show', course.id)
    else:
        form = LessonForm(instance=lesson)

    return render(request, 'courses/lesson_edit.html', {
        'form': form,
        'course': course,
    })


def lesson_delete(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    course = lesson.course

    if request.method == "POST":
        lesson.delete()
        messages.success(
            request, u"Lesson: {} was deleted".format(
                lesson.theme))
        return redirect('courses:show', course.id)

    return render(request, 'courses/lesson_delete.html', {
        'lesson': lesson,
        'course': course,
    })
