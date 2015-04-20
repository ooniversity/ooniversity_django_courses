from django.shortcuts import render
from courses.models import Course


def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def contact(request):
    return render(request, 'contact.html')


def coach_detail(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    courses_coach = Course.objects.filter(coach=coach_id)
    courses_assistant = Course.objects.filter(assistant=assistant_id)
    return render(request, 'coaches/coach_detail.html', {'coach': coach, 'courses_coach': courses_coach, 'courses_assistant': courses_assistant})
