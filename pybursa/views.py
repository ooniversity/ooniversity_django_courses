from django.shortcuts import render

#from courses import views           
from courses.models import Course
from django.views import generic



def courses_main(request):
    return render (request, 'index.html')

def contact_list(request):
    return render (request, 'contact.html')

def student_list(request):
    return render (request, 'student_list.html')

def student_detail(request):
    return render (request, 'student_detail.html')
