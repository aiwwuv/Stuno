from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from . models import Games

# Create your views here.


class HomeListView(ListView):
    model = Games
    template_name = 'home.html'

class AccCreateView(CreateView):
    model = Games
    template_name = 'account.html'
    fields = '__all__'

class TableView(ListView):
    model = Games
    template_name = 'table.html'

class BlogUpdateView(UpdateView):
    model = Games
    fields = ['type_game', 'points', 'time_game']
    template_name = 'edit.html'

class SpravkaView(ListView):
    model = Games
    template_name = 'spravka.html'

class KartiView(ListView):
    model = Games
    template_name = 'karti.html'

class GameView(ListView):
    model = Games
    template_name = 'game.html'

class PravView(ListView):
    model = Games
    template_name = 'prav.html'