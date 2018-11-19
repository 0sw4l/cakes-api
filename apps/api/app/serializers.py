from rest_framework import serializers

from apps.app.models import Cliente, ProductoPedido, Pedido


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'id',
            'cedula',
            'nombre',
            'telefono',
            'correo',
            'direccion'
        )


class PedidoSerializer(serializers.ModelSerializer):
    get_total = serializers.ReadOnlyField(source='total')

    class Meta:
        model = Pedido
        fields = (
            'id',
            'creacion',
            'actualizado',
            'cliente',
            'confirmado',
            'despachado',
            'get_total'
        )


class ProductoPedidosSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.ReadOnlyField(source='producto.nombre')
    total = serializers.ReadOnlyField(source='get_total')
    precio = serializers.ReadOnlyField(source='producto.precio')
    descripcion = serializers.ReadOnlyField(source='producto.descripcion')
    url = serializers.ReadOnlyField(source='producto.url_imagen')

    class Meta:
        model = ProductoPedido
        fields = (
            'id',
            'creacion',
            'actualizado',
            'producto',
            'producto_nombre',
            'url',
            'descripcion',
            'pedido',
            'precio',
            'cantidad',
            'total'
        )
