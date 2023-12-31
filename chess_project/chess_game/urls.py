from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from .views import GameListCreateView, MoveListCreateView, UserProfileDetailView, home_view, game_lobby_view, game_detail_view, CustomRegistrationView

urlpatterns = [
    path('api/games/', GameListCreateView.as_view(), name='game-list-create'),
    path('api/moves/', MoveListCreateView.as_view(), name='move-list-create'),
    path('api/userprofile/<int:pk>/', UserProfileDetailView.as_view(), name='userprofile-detail'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/register/', CustomRegistrationView.as_view, name='register'),
    path('main/', home_view, name='home-view'),
    path('game-lobby/', game_lobby_view, name='game-lobby-view'),
    path('game-detail/<int:game_id>/', game_detail_view, name='game-detail-view'),
 
]
