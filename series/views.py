from django.shortcuts import render
from django.views.generic import ListView

from .models import Series


class SeriesListView(ListView):
    model = Series


def index(request):
    featured_series = Series.objects.order_by('-name')[:2]

    context = {
        'featured_series': featured_series,
    }
    return render(request, 'index.html', context=context)
