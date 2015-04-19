from models import Coach
from courses.models import Course
from pybursa.utils import detail_view

def coach_d(request, pk):
    return detail_view(request, pk, Coach)
