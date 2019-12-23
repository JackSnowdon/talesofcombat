from django.urls import path
from .views import *

urlpatterns = [
    path('new_game/', new_game, name="new_game"),
    path('new_player/', new_player, name="new_player"),
    path(r'single_player/<int:pk>/', SinglePlayer.as_view(), name="single_player"),
    path(r'single_quest/<int:id>/', start_quest, name="start_quest"),
]