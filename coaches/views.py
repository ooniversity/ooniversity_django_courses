from django.shortcuts import render
from coaches.models import Coach

# Create your views here.
def coach(request, param):
	one_coach = Coach.objects.get(id__exact = int(param))
	c = {"coach": one_coach}
	return render(request, 'coach.html', c)
