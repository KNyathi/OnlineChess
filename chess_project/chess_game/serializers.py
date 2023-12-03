from rest_framework import serializers
from .models import Game, Move, User

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
        

class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = '_all_'  # Serialize all fields in the Move model
        

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '_all_'  # Serialize all fields in the UserProfile model
