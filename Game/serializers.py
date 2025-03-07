# serializers.py
from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [
            'GameID',
            'GameName',
            'Status',
            'Maxplayers',
            'StartCash',
            'Smallblind',
            'Raiseblind',
            'Timeout',
            'delay'
        ]
