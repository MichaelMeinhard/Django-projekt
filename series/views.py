from django.shortcuts import render
from django.views.generic import ListView

from .models import Series


class SeriesListView(ListView):
    model = Series


def index(request):
    return render(request, 'index.html', {})
