from django.urls import path
from .views import *

urlpatterns = [
    path('new_game/', new_game, name="new_game"),
]