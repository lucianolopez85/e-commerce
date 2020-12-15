from django.contrib import admin
from . import models


class CategoriaInline(admin.StackedInline):
    model = models.Categoria
    extra = 0


class VariacaoInline(admin.StackedInline):
    model = models.Variacao
    extra = 0


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao_curta',
                    'get_preco_formatado', 'get_preco_promocional_formatado', 'categoria']
    inlines = [
        VariacaoInline
    ]


admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Categoria)
admin.site.register(models.Variacao)
