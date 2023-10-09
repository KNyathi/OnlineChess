from django.db import models
from django.contrib.auth.models import User

class ChessGame(models.Model):
    # Define the chess game model, including game state, players, etc.
    # Add fields as needed based on your requirements.
    pass

class Player(models.Model):
    # Model to represent a player in a chess game
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add more fields like rating, game history, etc.

class Move(models.Model):
    # Model to store individual moves in a game
    game = models.ForeignKey(ChessGame, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    # Add fields for move details (start, end positions, piece moved, etc.)
