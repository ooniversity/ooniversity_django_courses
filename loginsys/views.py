# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from django.core.context_processors import csrf

User._meta.get_field('username')._unique = False


#Вход на сайт под своими учетными данными(залогиниться)
def login(request):
    context = {}
    #context.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            context['login_error'] = u'Такого пользователя не существует. Зарегистрируйтесь.'
            return render_to_response('loginsys/login.html', context)
    else:
        return render_to_response('loginsys/login.html', context)


#Выход (разлогиниться)
def logout(request):
    auth.logout(request)
    return redirect("/")

class MyRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label=u'Имя')
    last_name = forms.CharField(max_length=30, label=u'Фамилия')
    username = forms.CharField(max_length=30, label=u'Логин', required=True,)
    email = forms.EmailField(max_length=75, required=True)

    class Meta:
        model = User
        #fields = ("first_name", "last_name", "email",)
        fields = ("first_name", "last_name", "username", "email", "password1", "password2",)

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)

        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]
        #user.username = self.cleaned_data["username"]
        #user.password2 = self.cleaned_data["password2"]
        if commit:
            user.save()
        return user


def register(request):
    context = {}
    context['form'] = MyRegistrationForm()
    if request.POST:
        newuser_form = MyRegistrationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'],
                                        )
            auth.login(request, newuser)
            return redirect('/')
        else:
            context['form'] = newuser_form
    return render_to_response('loginsys/register.html', context)
