from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^pedido/', views.PedidoTemplateView.as_view(), name='pedido')
]
