from django.urls import path
from . import views

urlspatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
]