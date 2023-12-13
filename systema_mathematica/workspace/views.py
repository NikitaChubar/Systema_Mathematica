from django.http import HttpResponse
from django.shortcuts import render


def graph(request):
    context = {'check': 'Это строка для проверки работы контекста'}
    template_name = 'workspace/graph_page.html'
    return render(request, template_name, context)


def article(request, title):
    context = {'title': title}
    template_name = 'workspace/article_page.html'
    return render(request, template_name, context)
