from django.shortcuts import render
from courses.models import Course
from django.views.generic import TemplateView


class MixinCourseContext(object):
    def get_context_data(self, **kwargs):
        context = super(MixinCourseContext, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context


class IndexView(MixinCourseContext, TemplateView):
    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
        #  context = super(IndexView, self).get_context_data(**kwargs)
        #  context['courses'] = Course.objects.all()
        # return context


# class SomeTestView(View):
