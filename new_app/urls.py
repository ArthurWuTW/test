from django.urls import path, include
from . import views

urlpatterns = [
    path('',
        views.Page.as_view(),
        name='page'),
    path('calculateTopThree',
        views.CalculateTopThree.as_view(),
        name='calculateTopThree'),
]
