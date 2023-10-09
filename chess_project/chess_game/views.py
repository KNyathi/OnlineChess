from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ChessGame, Player, Move

def game_lobby(request):
    games = ChessGame.objects.all()
    return render(request, 'game_lobby.html', {'games': games})

def game_detail(request, game_id):
    game = get_object_or_404(ChessGame, id=game_id)
    return render(request, 'game_detail.html', {'game': game})


def profile(request):
    # Placeholder for user profile page
    return HttpResponse("User Profile Page- Welcome, {{request.user.username}}")
