from django.db import models
from django.urls import reverse


class TypeGame(models.Model):
    type_game = models.TextField()

    def __str__(self):
        return self.type_game


class Games(models.Model):
    user = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, verbose_name='Игрок')
    type_game = models.ForeignKey(
        TypeGame, on_delete=models.CASCADE, verbose_name='Тип игры')
    points = models.IntegerField(verbose_name='Очки')
    time_game = models.TimeField(verbose_name='Время игры')

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse('table')
# Create your models here.

