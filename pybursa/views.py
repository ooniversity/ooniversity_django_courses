from django.shortcuts import render

from courses.models import Course


def index_ooniversity(request):
    courses = Course.objects.all()
    return render(request, 'index_list.html', {'courses': courses})

def contact(request):
    return render(request, 'contact.html')
