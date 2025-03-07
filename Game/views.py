#make a game and join players until 10 players in  a game
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Game, Player
from .serializers import GameSerializer


class CreateGameView(APIView):
    
    def post(self,request):
        data = request.data
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

        









