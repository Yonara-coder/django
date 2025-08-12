from django.urls import path
from . import views


ultrapatterns = [
    path('', views.home),
    path('sobre/', views.sobre),
    path['contato/', views.contato],
    path['base/' views.base]
]
