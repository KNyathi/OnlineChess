from django.urls import path
from . import views

urlpatterns = [
    path('lobby/', views.game_lobby, name='game_lobby'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),
    path('profile/', views.profile, name='profile'),
]
