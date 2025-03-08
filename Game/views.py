# make a game and join players until 10 players in  a game
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Game, Player
from .serializers import GameSerializer
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError



class CreateGameView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = request.user
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            game = serializer.save()
            if Player.objects.filter(user=user).exists():
                player = Player.objects.get(user=user)
                player.game.add(game)
            else:
                player = Player.objects.create(user=user, cash=10000)
                player.game.add(game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class JoinGameView(APIView):

    def post(self, request):
        user = request.user
        data = request.data

        game_name = data.game_name
        game = Game.objects.get(GameName=game_name)
        if game.players.count() == 10:
            raise ValidationError("Max players cannot exceed 10")
        else:
            if Player.objects.filter(user=user).exists():
                player = Player.objects.get(user=user)
                player.game.add(game)
            else:
                player = Player.objects.create(user=user, cash=10000)
                player.game.add(game)
