from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as v

from jogos import views

urlpatterns = [
    path('', views.ver_jogos, name=''),
    path('classificacao', views.ver_classificacao, name='classificacao'),
    path('jogadores', views.ver_jogadores, name='ver_jogadores'),
    path('partida/<int:id_partida>/ganhador/<int:id_jogador>/', views.declarar_vencedor, name='resultado_partida'),
    path('jogador/<int:id_player>/mudar_nome/', views.ver_jogadores, name='mudar_nome'),
    path('login/', v.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', v.LogoutView.as_view(template_name='login.html'), name="logout"),
]
