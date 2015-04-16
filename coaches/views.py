#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django import forms
from django.forms.extras.widgets import SelectDateWidget

from static.python.AdminImageWidget import AdminImageWidget
from coaches.models import Coach
from courses.models import Course


birth_years = xrange(2015,1930,-1)


class CoachAddForm(forms.ModelForm):

    class Meta:
        model = Coach
        widgets = {'gender': forms.RadioSelect(), 'date_of_birth': SelectDateWidget(years=birth_years), 'image': AdminImageWidget()}
        labels = {'image': 'Photo'}
        fields = '__all__'



class CoachesView(generic.ListView):
    template_name = 'coaches/coaches.html'
    model = Coach


class CoachView(generic.ListView):
    template_name = 'coaches/coach.html'
    model = Coach

    def get_queryset(self):
        qs = super(CoachView, self).get_queryset().filter(pk=self.kwargs['pk'])
        return qs

def coach_add(request):
    context = dict()
    if request.method == 'POST':
        form = CoachAddForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()
            messages.success(request, 'Registration complite!')
            return redirect('coaches:coaches')
    else:
        form = CoachAddForm()
    context['form'] = form
    return render(request, 'coaches/add_coach.html', context)

def coach_edit(request, pk):
    application = Coach.objects.get(pk=pk)
    if request.method == 'POST':
        form = CoachAddForm(request.POST, request.FILES, instance=application)
        if form.is_valid():
            application = form.save()
            messages.success(request, 'Changes have been saved!')
    else:
        form = CoachAddForm(instance=application)
    return render(request, 'coaches/edit_coach.html', {'form': form, 'application': application})

def coach_remove(request, pk):
    application = Coach.objects.get(pk=pk)
    if request.method == 'POST':
        application.delete()
        messages.warning(request, u'Object {} {} deleted!'.format(application.user.last_name, application.user.first_name))
        return redirect('coaches:coaches')
    return render(request, 'coaches/delete_coach.html', {'application': application})
