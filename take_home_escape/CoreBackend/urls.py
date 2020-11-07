from django.urls import path

from . import views

urlpatterns = [
    path('', views.AboutUs, name='index'),
    path('manual/', views.ManualPage, name='manual'),
]