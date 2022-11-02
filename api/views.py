from question.models import generate_question
from django.http import JsonResponse
from .serializers import QuestionSerializer
from api.models import Game

def new_question(request):
    q = generate_question()
    return JsonResponse(QuestionSerializer(q).data)

def current_score(request):
    return JsonResponse({'score': request.session.get('score', 0)})

def average_score(request):
    games = Game.objects.all()
    s = 0
    for game in games:
        s += game.score 
    return JsonResponse({'average_score': '{:.2f}'.format(s / Game.objects.count())})

def highest_score(request):
	games = Game.objects.all()
	s = 0
	for game in games:
		if game.score > s:
			s = game.score
	return JsonResponse({'highest_score': s})