from django.shortcuts import render
from courses.models import Courses
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse

# Create your views here.
def index(request):
	cour = Courses.objects.all()
	templ = get_template('index.html')
	c = Context({"cour": cour})
	html = templ.render(c)
	return HttpResponse(html)
