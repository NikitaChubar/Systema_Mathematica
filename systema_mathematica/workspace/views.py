from django.http import HttpResponse
from django.shortcuts import render
from workspace.models import Article


def graph(request):
    articles = Article.objects.all()
    nodes = []
    links = []
    for art in articles:
        nodes.append({"id": art.pk, "label": art.title})
        for source in art.required_articles.split():
            links.append({"source": source, "target": art.pk})

    # Передайте данные в шаблон
    context = {
        'nodes': nodes,
        'links': links,
    }
    template_name = 'workspace/graph_page.html'
    return render(request, template_name, context)


def article(request, title):
    context = {'title': title}
    template_name = 'workspace/article_page.html'
    return render(request, template_name, context)
