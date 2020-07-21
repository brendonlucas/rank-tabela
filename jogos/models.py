from django.db import models


class Jogador(models.Model):
    nick = models.CharField(max_length=100)
    pontos = models.IntegerField(default=0)
    vitorias = models.IntegerField(default=0)
    partidas = models.IntegerField(default=0)


class Rodada(models.Model):
    name = models.CharField(max_length=100)


class Partida(models.Model):
    rodada = models.ForeignKey(Rodada, on_delete=models.CASCADE, related_name='partida')
    player1 = models.ForeignKey(Jogador, on_delete=models.CASCADE, related_name='play1')
    player2 = models.ForeignKey(Jogador, on_delete=models.CASCADE, related_name='play2')
    vencedor = models.IntegerField(default=0)



