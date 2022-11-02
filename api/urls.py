from rest_framework import routers
from .api import QuestionViewSet, PlayerViewSet, GameViewSet
from django.urls import path, include
from .views import new_question, current_score, average_score, highest_score

router = routers.DefaultRouter()
router.register('api/question', QuestionViewSet, 'questions')
router.register('api/player', PlayerViewSet, 'players')
router.register('api/game', GameViewSet, 'games')

urlpatterns = [
    path('', include(router.urls)),
    path('api/question/new', new_question),
    path('api/current_score', current_score),
    path('api/game/average_score', average_score),
    path('api/game/highest_score', highest_score)
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]