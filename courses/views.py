from django.shortcuts import render_to_response
from courses.models import Course

def course_view(request):
    model = Course.objects.all()
    return render_to_response('index.html', {'model': model})

def course_plan(request, pk):
    planmodel = Course.objects.get(pk=pk)
    lessons = planmodel.coursekey.all().order_by('order_number')
    return render_to_response('courses.html', {'planmodel': planmodel,
        'lessons': lessons,
        })