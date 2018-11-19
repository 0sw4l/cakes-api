from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify

from apps.utils.shortcuts import get_object_or_none


class Cliente(models.Model):
    cedula = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()
    direccion = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return '{} - {}'.format(
            self.nombre,
            self.telefono
        )


class Producto(models.Model):
    nombre = models.CharField(
        max_length=50,
        unique=True
    )
    url_imagen = models.URLField()
    precio = models.PositiveIntegerField()
    descripcion = models.TextField(
        blank=True,
        null=True
    )
    slug = models.SlugField(
        unique=True,
        editable=False
    )
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Producto'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    creacion = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    cliente = models.ForeignKey(Cliente)
    confirmado = models.BooleanField(default=False, editable=False)
    despachado = models.BooleanField(default=False, editable=False)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def total(self):
        return sum([
            p.get_total() for p in ProductoPedido.objects.filter(pedido=self)
        ])

    def add_product(self, id, cantidad):
        kwargs = {
            'producto_id': id,
            'pedido': self
        }
        product = get_object_or_none(
            ProductoPedido,
            **kwargs
        )
        if product:
            product.add_cantidad(cantidad)
        else:
            kwargs['cantidad'] = cantidad
            ProductoPedido.objects.create(
                **kwargs
            )

    def remove_product(self, id):
        kwargs = {
            'producto_id': id,
            'pedido': self
        }
        product = get_object_or_none(
            ProductoPedido,
            **kwargs
        )
        if product:
            product.delete()

    def detalle(self):
        return "\n".join(['{} - x{}, \n'.format(
            p.producto.nombre, p.cantidad
        ) for p in ProductoPedido.objects.filter(pedido=self)])

    def enviar(self):
        self.confirmado = True
        self.save()


class ProductoPedido(models.Model):
    creacion = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    producto = models.ForeignKey(Producto)
    pedido = models.ForeignKey(Pedido)
    cantidad = models.PositiveIntegerField()

    class Meta:
        unique_together = ['producto', 'pedido']
        verbose_name = 'Producto Pedido'
        verbose_name_plural = 'Productos Pedidos'

    def get_total(self):
        return self.producto.precio * self.cantidad

    def add_cantidad(self, cantidad):
        self.cantidad += cantidad
        self.save(update_fields=['cantidad'])

