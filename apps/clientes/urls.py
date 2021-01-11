# Python
# Django
from django.urls import path
# Project
from . import views


urlpatterns = [
  path('add/', views.ClienteCreateView.as_view(), name='cliente__cria'),
  path('<int:pk>/atualizar/', views.ClienteUpdateView.as_view(), name='cliente__atualiza'),
  path('<int:pk>/excluir/', views.ClienteDeleteView.as_view(), name='cliente__delete'),
  path('<int:pk>/', views.ClienteDetailView.as_view(), name='cliente__detail'),
  path('', views.ClienteListView.as_view(), name='cliente__list'),
]
