# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.contrib import messages
from django.contrib import auth
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from news.models import New
from courses.models import Course


# С помощью класса DetailView выводим информацию о конкретной новости на HTML страничку
class NewDetailView(DetailView):
    model = New

    def get_context_data(self, **kwargs):
        context = super(NewDetailView, self).get_context_data(**kwargs)
        new = get_object_or_404(New, pk = self.kwargs['pk'])
        if len(self.request.GET) >= 1:
            if self.request.GET['choice'] == u'like':
                new.likes+=1
                print 'Hello'
            else:
                new.dislikes+=1
            new.save()
        context['new'] = new
        courses = Course.objects.all()
        context['courses'] = courses
        context['username'] = auth.get_user(self.request).username
        return context


# С помощью класса ListView выводим список всех новостей на HTML страничку
class NewListView(ListView):
    model = New
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(NewListView, self).get_context_data(**kwargs)
        courses = Course.objects.all()
        context['courses'] = courses
        context['username'] = auth.get_user(self.request).username
        return context
    #def get_context_data(self, **kwargs):
     #   context = super(NewListView, self).get_context_data(**kwargs)
        #Сортировка новостей по дате публикации
      #  new_list = New.objects.order_by("date_public")[::-1]
       # context['new_list'] = new_list
        #return context



