from django.contrib import admin
from . import models


class ItemPedidoInline(admin.StackedInline):
    model = models.ItemPedido
    extra = 1


class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItemPedidoInline
    ]


admin.site.register(models.Pedido, PedidoAdmin)
admin.site.register(models.ItemPedido)
