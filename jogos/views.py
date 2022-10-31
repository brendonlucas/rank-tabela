from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.forms import Form
from django.shortcuts import render, redirect

from jogos.forms import JogadorForm
from jogos.models import Partida, Rodada, Jogador
from random import randint
import random


def get_user_logado(request):
    return request.user


def ver_jogos(request):
    rodadas = Rodada.objects.all()
    return render(request, 'jogos.html', {'partidas': rodadas, 'current_user': get_user_logado(request)})


def ver_jogadores(request):

    if get_user_logado(request).is_superuser:
        jogadores = Jogador.objects.all()
        return render(request, 'add_player.html', {'jogadores': jogadores, 'current_user': get_user_logado(request)})
    else:
        return redirect('')


def ver_classificacao(request):
    print(get_user_logado(request))
    #jogadores = Jogador.objects.all().order_by(Lower('nick').asc())

    jogadores = Jogador.objects.all().order_by('-pontos')
    return render(request, 'classificacao.html', {'jogadores': jogadores, 'current_user': get_user_logado(request)})


def mudar_nome(request, id_player):
    if get_user_logado(request).is_superuser:
        form = JogadorForm()
        jogador = Jogador.objects.get(id=id_player)
        if jogador:
            form = JogadorForm(request.POST)
            if form.is_valid():
                nome = form.cleaned_data['nome']
                jogador.nick = nome
                jogador.save()

        return redirect('ver_jogadores')

    else:
        return redirect('')


def make_partidas():
    jogadores = Jogador.objects.all()
    rodadas = Rodada.objects.all()
    partidas = Partida.objects.all()
    num_rodadas = 0
    jogos = []
    a = 0
    for i in range(1, jogadores.count() + 1):
        n_rodada = "Rodada " + str(i)
        num_rodadas += 1
        rodada = Rodada(name=n_rodada)

    ng = randint(1, 2)
    jogadores_n_escolhidos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    jogadores_n_escolhidos_2 = [1, 2, 3, 4, 5, 6, 7, 8]
    jogadores_ja_escolhidos = []

    for i in range(1, jogadores.count()):
        jogadores_ja_escolhidos.append(i)
        jogadores_n_escolhidos.remove(i)
        for f in range(len(jogadores_n_escolhidos)):
            print(i, "-", jogadores_n_escolhidos[f], )
            a += 1

        print()

    # n = randint(1, len(jogadores_n_escolhidos))
    print(a)


@login_required
def declarar_vencedor(request, id_partida, id_jogador):
    partida = Partida.objects.get(id=id_partida)
    jogador1 = Jogador.objects.get(id=partida.player1.id)
    jogador2 = Jogador.objects.get(id=partida.player2.id)
    print(partida.id)
    print(jogador1.nick)
    print(jogador2.nick)
    print(id_jogador)

    if id_jogador == 1:
        if partida.vencedor == 0:
            jogador1.vitorias += 1
            jogador1.pontos += 3
            partida.vencedor = 1
            jogador1.save()
            partida.save()

        elif partida.vencedor == 2:
            jogador1.vitorias += 1
            jogador1.pontos += 3
            jogador2.vitorias -= 1
            jogador2.pontos -= 3
            partida.vencedor = 1
            jogador1.save()
            jogador2.save()
            partida.save()

    elif id_jogador == 2:
        if partida.vencedor == 0:
            jogador2.vitorias += 1
            jogador2.pontos += 3
            partida.vencedor = 2
            jogador2.save()
            partida.save()

        elif partida.vencedor == 1:
            jogador2.vitorias += 1
            jogador2.pontos += 3
            jogador1.vitorias -= 1
            jogador1.pontos -= 3
            partida.vencedor = 2
            jogador1.save()
            jogador2.save()
            partida.save()

    return redirect('')
