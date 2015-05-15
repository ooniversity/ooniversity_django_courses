# -*- coding: utf-8 -*-
import random;

from django.shortcuts import render
from courses.models import Course
from photos.models import Photo
from news.models import New
#from pybursa import urls


def show_index(request):
    courses = Course.objects.all()
    try:
        with open('static/text.txt', 'r') as text_file:
            text = text_file.read().decode('utf-8')
    except IOError:
        print "Error! File text.txt not found."
    excerption = random.choice(text.split('\n'))
    number = text.split('\n').index(excerption)

    try:
        with open('static/autors_text.txt', 'r') as text_file:
            text = text_file.read()
    except IOError:
        print "Error! File autors_text.txt not found."
    autor = text.split('\n')[number]

    photo = random.choice(Photo.objects.all())

    #Вывод последних 10 новостей.
    last_news = New.objects.order_by("date_public")
    last_news = last_news[len(last_news)-10:]
    last_news = last_news[::-1]
    print last_news

    return render(request, 'index.HTML',
                 {'courses': courses, 'excerption': excerption,
                 'autor': autor, 'photo': photo, 'last_news': last_news})


def show_contacts(request):
    return render(request, 'contact.HTML')
