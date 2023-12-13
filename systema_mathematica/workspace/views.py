from django.http import HttpResponse
from django.shortcuts import render


def graph(request):
    return HttpResponse('<h1>Граф</h1>')


def article(request, title):
    return HttpResponse(f'<h1>Заголовок статьи: {title}</h1>')
