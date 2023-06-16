from django.shortcuts import render
from django.views.generic import ListView

from .models import Series


class SeriesListView(ListView):
    model = Series
    template_name = 'detail.html'
    context_object_name = 'series'


def index(request):
    featured_series = Series.objects.order_by('-name')[:3]
    longest_series = Series.objects.order_by('-length')[0]

    context = {
        'featured_series': featured_series,
        'longest_series': longest_series,
    }
    return render(request, 'index.html', context=context)


def series(request):
    context = {
        'series': Series.objects.all(),
    }
    return render(request, 'series.html', context=context)