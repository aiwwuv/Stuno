from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('account/', views.AccCreateView.as_view(), name='account'),
    path('table/', views.TableView.as_view(), name='table'),
    path('player/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='player_edit'),
    path('spravka/', views.SpravkaView.as_view(), name='spravka'),
    path('karti/', views.KartiView.as_view(), name='karti'),
    path('game/', views.GameView.as_view(), name='game'),
     path('prav/', views.PravView.as_view(), name='prav'),
]
