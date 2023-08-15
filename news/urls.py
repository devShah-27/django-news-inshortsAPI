from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('top/', views.top, name='top'),
    path('trending/', views.trending, name='trending'),
    path('science/', views.science, name='science'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('sports/', views.sports, name='sports'),
]

