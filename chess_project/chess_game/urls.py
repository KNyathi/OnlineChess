from django.urls import path
from .views import GameListCreateView

urlpatterns = [
    path('games/', GameListCreateView.as_view(), name='game-list-create'),
    # Add more URL patterns for other views as needed
]
