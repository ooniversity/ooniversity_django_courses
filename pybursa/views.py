from django.shortcuts import render
from django.http import HttpResponse


def show_index(request):
    return render(request, 'index.HTML')

def show_contacts(request):
    return render(request, 'contact.HTML')

def show_students(request):
    return render(request, 'student_list.HTML')

def show_student_detail(request):
    return render(request, 'student_detail.HTML')
