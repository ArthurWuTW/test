from django.urls import path, include
from . import views

urlpatterns = [
    path('',
        views.Page.as_view(),
        name='page'),
    path('removeOrderView/<str:order_name>/<str:order_number>',
        views.RemoveOrderView.as_view(),
        name='RemoveOrderView'),
]
