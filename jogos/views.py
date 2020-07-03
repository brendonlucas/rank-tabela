from django.shortcuts import render

from jogos.models import Partida, Rodada, Jogador


def ver_jogos(request):
    rodadas = Rodada.objects.all()
    return render(request, 'jogos.html', {'partidas': rodadas})


def ver_classificacao(request):
    jogadores = Jogador.objects.all()
    return render(request, 'classificacao.html', {'jogadores': jogadores})
