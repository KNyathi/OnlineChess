from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import GameListCreateView, MoveListCreateView, UserProfileDetailView, register_view, login_view

urlpatterns = [
    path('api/games/', GameListCreateView.as_view(), name='game-list-create'),
    path('api/moves/', MoveListCreateView.as_view(), name='move-list-create'),
    path('api/userprofile/<int:pk>/', UserProfileDetailView.as_view(), name='userprofile-detail'),
    path('login/', login_view.as_view(), name='login'),
    path('register/', register_view, name='register'),
    # Add more URL patterns for other views as needed
]
