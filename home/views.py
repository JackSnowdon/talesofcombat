from django.shortcuts import render
from setup.models import BaseModel

# Create your views here.

def index(request):
    players = BaseModel.objects.order_by("name")
    return render(request, 'index.html', {"players": players})