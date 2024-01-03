from django.http import HttpResponse
from django.shortcuts import render
import json


def graph(request):
    nodes = [
        {"id": 1, "label": "Node1"},
        {"id": 2, "label": "Node2"},
        {"id": 3, "label": "Node3"},
        {"id": 4, "label": "Node4"},
        {"id": 5, "label": "Node5"},
        {"id": 6, "label": "Node6"},
        {"id": 7, "label": "Node7"},
        {"id": 8, "label": "Node8"},
        {"id": 9, "label": "Node9"},
        {"id": 10, "label": "Node10"},
    ]

    links = [
        {"source": 5, "target": 10},
        {"source": 5, "target": 4},
        {"source": 6, "target": 2},
        {"source": 5, "target": 6},
        {"source": 2, "target": 4},
        {"source": 8, "target": 7},
        {"source": 10, "target": 9},
        {"source": 10, "target": 1},
        {"source": 4, "target": 3},
        {"source": 7, "target": 4},
    ]

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
