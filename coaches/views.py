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
from django.contrib.auth.models import User


birth_years = xrange(2015, 1930, -1)


class UserAddForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        help_texts = {
            'username': 'This field may already be filled in user settings!',
            'first_name': 'This field may already be filled in user settings!',
            'last_name': 'This field may already be filled in user settings!',
            'email': 'This field may already be filled in user settings!',
        }


class CoachAddForm(forms.ModelForm):

    class Meta:
        model = Coach
        fields = '__all__'
        widgets = {
            'gender': forms.RadioSelect(),
            'date_of_birth': SelectDateWidget(years=birth_years),
            'image': AdminImageWidget()
        }
        labels = {'image': 'Photo'}
        help_texts = {'address': 'Not a required field.'}


class CoachEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # magic
        try:
            self.user = kwargs['instance'].user
        except KeyError:
            self.user = None
        user_kwargs = kwargs.copy()
        user_kwargs['instance'] = self.user
        self.uf = UserForm(*args, **user_kwargs)
        # magic end

        super(CoachEditForm, self).__init__(*args, **kwargs)

        self.fields.update(self.uf.fields)
        self.initial.update(self.uf.initial)

    def save(self, *args, **kwargs):
        # save both forms
        self.uf.save(*args, **kwargs)
        return super(CoachEditForm, self).save(*args, **kwargs)

    class Meta:
        model = Coach
        exclude = ['user']
        widgets = {
            'gender': forms.RadioSelect(),
            'date_of_birth': SelectDateWidget(years=birth_years),
            'image': AdminImageWidget()
        }
        labels = {'image': 'Photo'}
        help_texts = {'address': 'Not a required field.'}


class CoachesView(generic.ListView):
    template_name = 'coaches/coaches.html'
    model = Coach


class CoachView(generic.ListView):
    template_name = 'coaches/coach.html'
    model = Coach

    def get_queryset(self):
        qs = super(CoachView, self).get_queryset().filter(pk=self.kwargs['pk'])
        return qs


def user_add(request):
    context = dict()
    if request.method == 'POST':
        user_form = UserAddForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            messages.success(request, 'User registration complite!')
            return redirect('coaches:coaches')
    else:
        user_form = UserAddForm()
    context['userform'] = user_form
    return render(request, 'coaches/add_user.html', context)


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
        form = CoachEditForm(request.POST, request.FILES, instance=application)
        if form.is_valid():
            application = form.save()
            messages.success(request, 'Changes have been saved!')
    else:
        form = CoachEditForm(instance=application)
    application = Coach.objects.get(pk=pk)
    return render(request, 'coaches/edit_coach.html', {'form': form, 'application': application})


def coach_remove(request, pk):
    application = Coach.objects.get(pk=pk)
    if request.method == 'POST':
        application.delete()
        messages.warning(request, u'Object {} {} deleted!'.format(application.user.last_name, application.user.first_name))
        return redirect('coaches:coaches')
    return render(request, 'coaches/delete_coach.html', {'application': application})
