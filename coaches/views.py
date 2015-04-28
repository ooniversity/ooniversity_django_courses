from django.shortcuts import render

from coaches.models import Coach


def coach_info(request, coach_id):
	return render (request, 'coaches/coach_page.html',
	{'coach_info': Coach.objects.get(id=coach_id)})
