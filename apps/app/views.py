from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from apps.app.models import Producto


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Producto.objects.all()
        return context


class PedidoTemplateView(TemplateView):
    template_name = 'cart.html'


