from django.shortcuts import render, redirect
from courses.models import Course
from courses.models import Lesson
from coaches.models import Coach
from django import forms

def course (request):
    courses = Course.objects.all()
    return render(request, 'index_list.html', 
                  {'courses':courses})


def lesson_pd (request):
    lessons = Lesson.objects.filter(course_id=4)
    coaches = Coach.objects.all()
    return render(request, 'pd.html', 
                  {'lessons': lessons, 'coaches': coaches})



def lesson_js (request):
    lessons = Lesson.objects.filter(course__id=5)
    coaches = Coach.objects.all()
    return render(request, 'js.html', 
                  {'lessons':lessons, 'coaches': coaches})


def lesson_rr (request):
    lessons = Lesson.objects.filter(course__id=6)
    coaches = Coach.objects.all()
    return render(request, 'rr.html', 
                  {'lessons':lessons, 'coaches': coaches})

class LessonForm(forms.ModelForm):
      class Meta:
            model = Lesson  
    


def add_lesson(request):
    if request.method == "POST":
        model_form = LessonForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            return redirect('home')
    else:
        model_form = LessonForm()
    
    return render(request, 'add_lesson.html', 
                    {'model_form':model_form}
      )
