from django.urls import path, register_converter
from .views import (
    HomePageView,
    AboutPageView,
    HeroListApiView,
    HeroDetailApiView,
    PlayerListApiView,
    PlayerDetailApiView,
)
from . import views, converts


# convert Float URL
register_converter(converts.FloatUrlParameterConverter, "float")

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("heroes/<int:id>/", views.hero_detail, name="hero_detail"),
    path("players/<float:id>/", views.player_detail, name="player_detail"),
    path("api/heroes", HeroListApiView.as_view()),
    path("api/heroes/<int:id>", HeroDetailApiView.as_view()),
    path("api/players", PlayerListApiView.as_view()),
    path("api/players/<int:id>", PlayerDetailApiView.as_view()),
]
