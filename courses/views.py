from django.shortcuts import render_to_response
from courses.models import Course, Lesson


def course_view(request):
    model = Course.objects.all()
    print model
    return render_to_response('index.html', {'model': model})

def course_plan(request):
    planmodel = Lesson.objects.all().order_by('order_number')
    model = Course.objects.all()
    matches = list(chain(model, planmodel))
    return render_to_response('courses.html',{'matches': matches})