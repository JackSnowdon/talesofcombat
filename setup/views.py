from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import DetailView
from .models import *
from .forms import *

# Create your views here.

def new_game(request):
    players = BaseModel.objects.order_by("name")
    return render(request, 'new_game.html', {"players": players})

def new_player(request):
    if request.method == "POST":
        player_form = NewBaseForm(request.POST)
        if player_form.is_valid():
            player = player_form.save(commit=False)
            player.soul = 0

            power = int(request.POST.get('power'))
            defence = int(request.POST.get('defence'))
            social = int(request.POST.get('social'))
            magik = int(request.POST.get('magik'))
            wisdom = int(request.POST.get('wisdom'))
            dex = int(request.POST.get('dex'))
            
            stat_total = power + defence + social + magik + wisdom + dex

            race_id = int(request.POST.get('race'))
            race = Race.objects.get(id=race_id)

            if stat_total > 100:
                messages.error(request, 'Invalid Stats for {0}, stat total ({1}) greater than 100'.format(player.name, stat_total), extra_tags='alert')
            else:
                player.max_hp = race.buffs * (defence + power)
                player.max_mp = race.buffs * (wisdom + magik)
                player.save()
                messages.error(request, 'Added {0}'.format(player.name), extra_tags='alert')
                return redirect("new_game")

    else:
        player_form = NewBaseForm()
    return render(request, "new_player.html", {"player_form": player_form })


class SinglePlayer(DetailView):
    model = BaseModel

