from django.forms import *
from django import forms


class JogadorForm(forms.Form):
    nome = forms.CharField(required=True)