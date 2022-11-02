from question.models import Question, Player
from api.models import Game 
from rest_framework import viewsets, permissions
from .serializers import QuestionSerializer, PlayerSerializer, GameSerializer

# Question Viewset

class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all()
	permission_classes = [
		permissions.AllowAny
	]
	serializer_class = QuestionSerializer
 

class PlayerViewSet(viewsets.ModelViewSet):
	queryset = Player.objects.all()
	permission_classes = [
		permissions.AllowAny
	]
	serializer_class = PlayerSerializer
 
class GameViewSet(viewsets.ModelViewSet):
	queryset = Game.objects.all()
	permission_classes = [
		permissions.AllowAny
	]
	serializer_class = GameSerializer