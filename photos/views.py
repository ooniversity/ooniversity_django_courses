# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib import auth
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from photos.models import Photo
from courses.models import Course


# С помощью класса ListView выводим список всех фотографий на HTML страничку
class PhotoListView(ListView):
    model = Photo

    def get_context_data(self, **kwargs):
        context = super(PhotoListView, self).get_context_data(**kwargs)
        courses = Course.objects.all()
        context['courses'] = courses
        context['username'] = auth.get_user(self.request).username
        return context


class PhotoDetailView(DetailView):
    model = Photo

    def get_context_data(self, **kwargs):
        context = super(PhotoDetailView, self).get_context_data(**kwargs)
        courses = Course.objects.all()
        context['courses'] = courses
        photos = Photo.objects.all()
        context['photos'] = photos
        context['username'] = auth.get_user(self.request).username
        return context
