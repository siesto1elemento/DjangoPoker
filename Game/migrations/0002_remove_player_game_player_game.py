# Generated by Django 5.1.6 on 2025-03-07 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Game", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="player",
            name="game",
        ),
        migrations.AddField(
            model_name="player",
            name="game",
            field=models.ManyToManyField(related_name="players", to="Game.game"),
        ),
    ]
