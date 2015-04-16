from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from courses.models import Course, Lesson
from students.models import Student 
from coaches.models import Coach
from datetime import datetime


def show_index(request):
	courses = Course.objects.all()
	return render(request, 'index.html', {'courses': courses})
    

def contacts(request):
	return render(request, 'contacts.html', {'date_now': datetime.now()})


def show_coach(request, id):
    coach = Coach.objects.get(id = int(id))
    courses = Course.objects.all()
    teacher = []
    assistant = []
    for i in courses:
        if coach.user == i.teacher.user:
            teacher.append(i)
    for i in courses:
        if coach.user == i.assistant.user:
            assistant.append(i)
    return render(request, 'coaches/coach.html', {'coach': coach, 'teacher': teacher, 
                                                  'assistant': assistant})