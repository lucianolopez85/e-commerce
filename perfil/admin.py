from django.contrib import admin
from . import models


class EnderecoInline(admin.StackedInline):
    model = models.Endereco
    extra = 0


class ContatoInline(admin.StackedInline):
    model = models.Contato
    extra = 0


class PerfilAdmin(admin.ModelAdmin):
    inlines = [
        ContatoInline,
        EnderecoInline
    ]


admin.site.register(models.Perfil, PerfilAdmin)
admin.site.register(models.Contato)
admin.site.register(models.Endereco)
