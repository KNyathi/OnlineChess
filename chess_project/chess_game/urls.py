from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import GameListCreateView, MoveListCreateView, UserProfileDetailView, register_view, login_view, home_view, game_lobby_view, game_detail_view, profile_view

urlpatterns = [
    path('api/games/', GameListCreateView.as_view(), name='game-list-create'),
    path('api/moves/', MoveListCreateView.as_view(), name='move-list-create'),
    path('api/userprofile/<int:pk>/', UserProfileDetailView.as_view(), name='userprofile-detail'),
    path('login/', login_view.as_view(), name='login'),
    path('register/', register_view, name='register'),
    path('home/', home_view, name='home-view'),
    path('game-lobby/', game_lobby_view, name='game-lobby-view'),
    path('game-detail/', game_detail_view, name='game-detail-view'),
    path('profile/', profile_view, name='profile-view'),
    # Add more URL patterns for other views as needed
]
