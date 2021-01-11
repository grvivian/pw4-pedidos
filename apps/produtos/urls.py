# Python
# Django
from django.urls import path
# Project
from . import views


urlpatterns = [
  path('add/', views.ProdutoCreateView.as_view(), name='produto__cria'),
  path('<int:pk>/atualizar/', views.ProdutoUpdateView.as_view(), name='produto__atualiza'),
  path('<int:pk>/excluir/', views.ProdutoDeleteView.as_view(), name='produto__delete'),
  path('<int:pk>/', views.ProdutoDetailView.as_view(), name='produto__detail'),
  path('', views.ProdutoListView.as_view(), name='produto__list'),
]
