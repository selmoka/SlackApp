from django.urls import path, reverse

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]