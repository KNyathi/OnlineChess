from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Game, User, Move
from .serializers import GameSerializer, UserProfileSerializer, MoveSerializer
from rest_framework import generics
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import CreateGameForm, MakeMoveForm
from django.db.models import Q
import chess
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


# 1) Home View
def home_view(request):
    # Any logic to prepare data for the homepage goes here

    # Check if the user is authenticated
    user = request.user if request.user.is_authenticated else None

    # Retrieve recent game activity (placeholder example)
    recent_activity = [
        {'user': 'User1', 'move': 'e4', 'game_id': 1},
        {'user': 'User2', 'move': 'Nf6', 'game_id': 2},
        # Add more recent activities as needed
    ]

    context = {
        'user': user,
        'recent_activity': recent_activity,
    }

    return render(request, 'index.html', context)




# 2) Game Lobby View
def game_lobby_view(request):
    # Handle listing, creating, and joining games
    # Render the game lobby page

    # 1. List Available Games
    available_games = Game.objects.filter(is_active=True)

    # 2. Create New Games
    if request.method == 'POST':
        create_game_form = CreateGameForm(request.POST)
        if create_game_form.is_valid():
            new_game = create_game_form.save()
            # Redirect the user to the game detail page for the new game
            return redirect('game-detail-view', game_id=new_game.id)
    else:
        create_game_form = CreateGameForm()

    # 3. Joining Existing Games
    if request.method == 'POST':
        game_id = request.POST.get('game_id')
        game_to_join = Game.objects.get(pk=game_id)
        if game_to_join.is_active and not game_to_join.is_full():
            # Logic for joining the game, update game state, and redirect to the game detail page
            # You may need to implement specific game join logic here
	        game_to_join.player2 = request.user
	        game_to_join.save()
	    
	        return redirect('game-detail-view', game_id=game_id)
	    	
    context = {
        'available_games': available_games,
        'create_game_form': create_game_form,
    }

    return render(request, 'game_lobby.html', context)




# 3) Game Detail View
def game_detail_view(request, game_id):
    # Retrieve the game with game_id and render its details

    # Retrieve the specific game using the game_id
    game = get_object_or_404(Game, pk=game_id)

    # Retrieve the moves for this game
    moves = Move.objects.filter(game=game)

    # 1. Display Chessboard (You'll need to implement the chessboard display logic)
    board_id = f'chessboard-{game_id}'  # Create a unique ID for the chessboard container

    # 2. Display Player Information
    player1 = game.player1
    player2 = game.player2

    # 3. Handling Moves
    if request.method == 'POST':
        make_move_form = MakeMoveForm(request.POST)
        if make_move_form.is_valid():
            move = make_move_form.save(commit=False)
            move.game = game
            move.save()
            # Add logic to update the game state based on the move
            # Redirect to the game detail page

    else:
        make_move_form = MakeMoveForm()

    context = {
        'game': game,
        'player1': player1,
        'player2': player2,
        'moves': moves,
        'make_move_form': make_move_form,
        'board_id': board_id,  # Pass the chessboard container's ID
    }

    return render(request, 'game_detail.html', context)




# 4) Profile View
def profile_view(request, user_id):
    # Retrieve the user's profile using the user_id
    user_profile = get_object_or_404(UserProfile, user_id=user_id)

    # Retrieve game history for the user
    game_history = Game.objects.filter(Q(player1=user_profile.user) | Q(player2=user_profile.user))

    context = {
        'user_profile': user_profile,
        'game_history': game_history,
    }

    return render(request, 'profile.html', context)




# 5) API Views
class CustomRegistrationView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration

class GameListCreateView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class MoveListCreateView(generics.ListCreateAPIView):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer


class UserProfileDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
