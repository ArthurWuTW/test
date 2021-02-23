from django.urls import path, include
from . import views

urlpatterns = [
    path('page',
        views.Page.as_view(),
        name='page')
]
