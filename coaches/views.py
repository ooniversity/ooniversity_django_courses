from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from coaches.models import Coach


class IndexView(generic.ListView):
    template_name = 'coaches/index.html'
    context_object_name = 'coach_list'

    def get_queryset(self):
        return Coach.objects.order_by('-id')[:5]

class DetailView(generic.DetailView):
    model = Coach
    template_name = 'coaches/detail.html'




