from django.shortcuts import render
from coaches.models import Coach


def coaches_info(request, coach_id):
    coaches_info = Coach.objects.get(id=coach_id)
    
    
    return render(request, 'coaches/coaches_info.html', { 'coaches_info': coaches_info})

