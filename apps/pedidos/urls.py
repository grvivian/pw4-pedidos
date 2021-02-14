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
  path('<int:pk>/fechar/', views.FecharPedidoView.as_view(), name='pedido__fechar'),
  path('<int:pk>/enviar/', views.EnviarPedidoView.as_view(), name='pedido__enviar'),
  path('<int:pk>/', views.PedidoDetailView.as_view(), name='pedido__detail'),
  path('fechados', views.PedidoFechadoListView.as_view(), name='pedido__list__fechado'),
  path('enviados/', views.PedidoEnviadoListView.as_view(), name='pedido__list__enviado'),
  path('', views.PedidoCriadoListView.as_view(), name='pedido__list'),
]
