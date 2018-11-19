from django.conf.urls import url, include
from rest_framework import routers
from . import views, viewsets

router = routers.DefaultRouter()
router.register(r'pedidos', viewsets.PedidoViewSet)

urlpatterns = [
    url(r'^enviar-cliente/', views.ClienteView.as_view()),
    url(r'^viewsets/', include(router.urls))
]

