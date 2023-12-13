from django.urls import path
from . import views

urlpatterns = [
    path('', views.graph, name='graph'),
    path('<slug:title>/', views.article)
]
