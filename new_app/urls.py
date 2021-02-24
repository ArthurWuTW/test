from django.urls import path, include
from . import views

urlpatterns = [
    path('',
        views.Page.as_view(),
        name='page'),
    path('removeOrderView',
        views.RemoveOrderView.as_view(),
        name='removeOrderView'),
]
