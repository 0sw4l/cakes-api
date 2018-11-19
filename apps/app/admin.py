from django.contrib import admin
from . import models
# Register your models here.
admin.site.site_header = 'AmisCake Admin'
admin.site.site_title = 'AmisCake Admin'
admin.site.index_title = 'AmisCake Admin'


@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'precio',
        'url_imagen',
        'slug',
        'activo',
    ]


@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'cedula',
        'nombre',
        'telefono',
        'correo',
        'direccion'
    ]
    search_fields = list_display


@admin.register(models.Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'creacion',
        'actualizado',
        'cliente',
        'confirmado',
        'despachado',
        'detalle'
    ]