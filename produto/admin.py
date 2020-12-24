from django.contrib import admin
from . import models


class CategoriaInline(admin.StackedInline):
    model = models.Categoria
    extra = 0


class VariacaoInline(admin.StackedInline):
    model = models.Variacao
    extra = 0


class SubcategInline(admin.StackedInline):
    model = models.Subcateg
    extra = 0


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao_curta',
                    'preco_marketing', 'preco_marketing_promocional', 'slug', 'categoria']
    inlines = [
        VariacaoInline
    ]


admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Categoria)
admin.site.register(models.Variacao)
admin.site.register(models.Subcateg)
