# Python
# Django
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Project

class PedidosHome(LoginRequiredMixin, TemplateView):
    template_name = "pedidos/pedidos.html"
