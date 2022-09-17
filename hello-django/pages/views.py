from django.views.generic import TemplateView
from django.shortcuts import render
from django.db import connection
from pages.models import Hero, Player
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import HeroSerializer, PlayerSerializer


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


def hero_detail(request, id):
    """
    Django query model
    """
    hero_objs = Hero.objects.get(pk=id)
    context = {"hero": hero_objs}
    # hero_json = serializers.serialize("json", [hero_objs])
    # print(hero_json)
    return render(request, "hero_detail.html", context)


def player_detail(request, id):
    # player_objs = Hero.objects.get(pk=id)

    raw_query = f"select * from public.player where player_id={id}"
    # print("QUERY", raw_query)

    with connection.cursor() as cursor:
        cursor.execute(raw_query)
        # cursor.fetchall()
        result = cursor.fetchone()
        print(result)

    player_objs = Player()
    player_objs.player_id = result[0]
    player_objs.rank_tier = result[1]
    player_objs.win = result[2]
    player_objs.lose = result[3]
    player_objs.mmr_estimate = result[4]

    context = {"player": player_objs}
    return render(request, "player_detail.html", context)


# ------------ Heros API ------------- #


class HeroListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        List all the Hero items
        """
        heroes = Hero.objects.all()
        serializer = HeroSerializer(heroes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create the Hero with given Hero data
        """
        data = {
            "hero_id": request.data.get("hero_id"),
            "hero_name": request.data.get("hero_name"),
            "pro_win": request.data.get("pro_win"),
            "pro_pick": request.data.get("pro_pick"),
        }
        serializer = HeroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HeroDetailApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]

    def get_object(self, id):
        try:
            return Hero.objects.get(hero_id=id)
        except Hero.DoesNotExist:
            return None

    # 1. Get a the Hero items
    def get(self, request, id, *args, **kwargs):
        """
        Get a the Hero items via Id
        """
        hero_instance = self.get_object(id)
        if not hero_instance:
            return Response(
                {"message": "Object with hero id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = HeroSerializer([hero_instance], many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, id, *args, **kwargs):
        """
        Updates the Hero item with given id if exists
        """
        hero_instance = self.get_object(id)
        if not hero_instance:
            return Response(
                {"message": "Object with hero id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = {
            "hero_name": request.data.get("hero_name"),
            "pro_win": request.data.get("pro_win"),
            "pro_pick": request.data.get("pro_pick"),
        }
        serializer = HeroSerializer(instance=hero_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, id, *args, **kwargs):
        """
        Deletes the hero item with given id if exists
        """
        hero_instance = self.get_object(id)
        if not hero_instance:
            return Response(
                {"message": "Object with hero id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        hero_instance.delete()
        return Response({"message": "Object deleted!"}, status=status.HTTP_200_OK)


# ------------ Players API ------------- #


class PlayerListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        List all the Hero items
        """
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create the Hero with given Hero data
        """
        data = {
            "player_id": request.data.get("player_id"),
            "rank_tier": request.data.get("rank_tier"),
            "win": request.data.get("win"),
            "lose": request.data.get("lose"),
            "mmr_estimate": request.data.get("mmr_estimate"),
        }
        serializer = PlayerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlayerDetailApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]

    def get_object(self, id):
        try:
            return Player.objects.get(player_id=id)
        except Player.DoesNotExist:
            return None

    # 1. Get a the Hero items
    def get(self, request, id, *args, **kwargs):
        """
        Get a the Hero items via Id
        """
        player_instance = self.get_object(id)
        if not player_instance:
            return Response(
                {"message": "Object with player id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = PlayerSerializer(player_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, id, *args, **kwargs):
        """
        Updates the Hero item with given id if exists
        """
        player_instance = self.get_object(id)
        if not player_instance:
            return Response(
                {"message": "Object with player id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = {
            "rank_tier": request.data.get("rank_tier"),
            "win": request.data.get("win"),
            "lose": request.data.get("lose"),
            "mmr_estimate": request.data.get("mmr_estimate"),
        }
        serializer = PlayerSerializer(instance=player_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, id, *args, **kwargs):
        """
        Deletes the hero item with given id if exists
        """
        player_instance = self.get_object(id)
        if not player_instance:
            return Response(
                {"message": "Object with player id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        player_instance.delete()
        return Response({"message": "Object deleted!"}, status=status.HTTP_200_OK)
