from django.shortcuts import render
from django.views import generic

def contact(request):
    return render(request,'contact.html')

def student_l(request):
    return render(request,'student_list.html')


