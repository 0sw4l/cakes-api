from rest_framework import generics
from rest_framework.decorators import detail_route
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from apps.api.app.serializers import PedidoSerializer, ProductoPedidosSerializer
from apps.app.models import ProductoPedido, Pedido
from apps.utils.shortcuts import get_object_or_none


class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def get_item(self, id):
        return get_object_or_none(Pedido, id=id)

    def create(self, request, *args, **kwargs):
        pedido = Pedido.objects.create(
            cliente_id=request.data['cliente_id']
        )
        return Response({
            'id': pedido.id
        })

    @detail_route(methods=['POST'])
    def add_product(self, request, pk=None):
        product = int(request.data['product_id'])
        cantidad = int(request.data['cantidad'])
        pedido = self.get_item(pk)
        if pedido:
            pedido.add_product(product, cantidad)
        return Response({
            'success': True
        })

    @detail_route(methods=['POST'])
    def remove_product(self, request, pk=None):
        product = int(request.data['product_id'])
        pedido = self.get_item(pk)
        if pedido:
            pedido.remove_product(product)
        return Response({
            'success': True
        })

    @detail_route(methods=['GET'])
    def items(self, request, pk=None):
        pedido = self.get_item(pk)
        productos = ProductoPedido.objects.filter(
            pedido_id=pk
        )
        serializer = ProductoPedidosSerializer(productos, many=True)
        return Response({
            'id': pedido.id,
            'total': pedido.total(),
            'productos': serializer.data
        })

    @detail_route(methods=['POST'])
    def send(self, request, pk=None):
        pedido = self.get_item(pk)
        if pedido:
            pedido.enviar()
        return Response({
            'success': True
        })


