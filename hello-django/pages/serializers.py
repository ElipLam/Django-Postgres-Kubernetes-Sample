from rest_framework import serializers
from .models import Hero, Player


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ["hero_id", "hero_name", "pro_win", "pro_pick"]


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["player_id", "rank_tier", "win", "lose", "mmr_estimate"]
