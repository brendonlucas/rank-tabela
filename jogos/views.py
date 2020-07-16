from django.db.models.functions import Lower
from django.forms import Form
from django.shortcuts import render, redirect

from jogos.forms import JogadorForm
from jogos.models import Partida, Rodada, Jogador


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
    jogadores = Jogador.objects.all().order_by(Lower('nick').asc())

    # jogadores = Jogador.objects.all().order_by('pontos')
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
