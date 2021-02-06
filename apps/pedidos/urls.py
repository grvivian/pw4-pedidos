# Python
# Django
from django.urls import path
# Project
from . import views


urlpatterns = [
  path('item/<int:pedido>/', views.ItemCreateView.as_view(), name='pedido__add__item'),
  path('item/<int:pk>/atualizar/', views.ItemUpdateView.as_view(), name='pedido__atualiza__item'),
  path('item/<int:pk>/excluir/', views.ItemDeleteView.as_view(), name='pedido__excluir__item'),
  path('add/', views.PedidoCreateView.as_view(), name='pedido__cria'),
  path('<int:pk>/atualizar/', views.PedidoUpdateView.as_view(), name='pedido__atualiza'),
  path('<int:pk>/excluir/', views.PedidoDeleteView.as_view(), name='pedido__delete'),
  path('<int:pk>/', views.PedidoDetailView.as_view(), name='pedido__detail'),
  path('', views.PedidoListView.as_view(), name='pedido__list'),
]
