from django.shortcuts import render

# Create your views here.

def new_game(request):
    return render(request, 'new_game.html')