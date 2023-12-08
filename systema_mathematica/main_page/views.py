from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # Переменная request содержит всю информацию о запросе

    # HttpResponse - это возвращаемая страница
    return HttpResponse("<h1>Главная страница, мазафака!</h1>")
