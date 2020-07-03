from django.contrib import admin
from django.urls import path

from jogos import views

urlpatterns = [
    path('', views.ver_jogos, name=''),
    path('classificacao', views.ver_classificacao, name='classificacao'),
]
