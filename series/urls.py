from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('series/', views.series, name='series'),
    path('series/<int:pk>', views.SeriesListView.as_view(), name='detail_series')
]
