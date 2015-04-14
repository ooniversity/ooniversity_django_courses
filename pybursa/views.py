from django.shortcuts import render, get_object_or_404

from coaches.models import Coach

def index(request):
    return render(request, 'index.html')


def contact(request):
    c = get_object_or_404(Coach, pk=1)
    return render(request, 'contact.html', {'coach': c
                                            })


def student_list(request):
    return render(request, 'student_list.html')


def student_detail(request):
    return render(request, 'student_detail.html')




