# Generated by Django 3.0.8 on 2020-07-03 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0003_rodada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='rodada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rodadas', to='jogos.Jogador'),
        ),
    ]
