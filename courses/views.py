from django.shortcuts import render
from courses.models import Course
from courses.models import Lesson
from coaches.models import Coach
from django import forms

def course (request):
    courses = Course.objects.all()
    return render(request, 'index_list.html', 
                  {'courses':courses})


def lesson_pd (request):
    lessons = Lesson.objects.filter(course__id=1)
    coaches = Coach.objects.all()
    return render(request, 'pd.html', 
                  {'lessons': lessons, 'coaches': coaches})



def lesson_js (request):
    lessons = Lesson.objects.filter(course__id=2)
    coaches = Coach.objects.all()
    return render(request, 'js.html', 
                  {'lessons':lessons, 'coaches': coaches})


def lesson_rr (request):
    lessons = Lesson.objects.filter(course__id=3)
    coaches = Coach.objects.all()
    return render(request, 'rr.html', 
                  {'lessons':lessons, 'coaches': coaches})

class LessonForm(forms.ModelForm):
      class Meta:
            model = Lesson  
    


def add_lesson(request):
    model_form = LessonForm()
    return render(request, 'add_lesson.html', 
                    {'model_form':model_form}
      )
