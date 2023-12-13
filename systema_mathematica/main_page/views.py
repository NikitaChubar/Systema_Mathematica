from django.shortcuts import render


def index(request):
    context = None
    template_name = 'main_page/main_page.html'
    return render(request, template_name, context)
