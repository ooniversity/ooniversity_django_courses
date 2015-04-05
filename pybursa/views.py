from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def student_l(request):
    return render(request,'student_list.html')

def student_d(request):
    return render(request,'student_detail.html')
