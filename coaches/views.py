from django.shortcuts import get_object_or_404, render

from coaches.models import Coach


def coaches_detail(request, coach_id):
    c = get_object_or_404(Coach, pk=coach_id)
    template_name = 'coaches/detail_coach.html'
    return render(request, template_name, {'coaches': c
                                           })

