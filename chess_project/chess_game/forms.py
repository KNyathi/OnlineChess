from django import forms
from .models import Game, Move

class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['player1', 'player2']  # Add more fields if needed

class MakeMoveForm(forms.ModelForm):
    class Meta:
        model = Move
        fields = ['move_text']  # Adjust the field(s) based on your Move model
