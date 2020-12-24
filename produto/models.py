from django.conf import settings
import os
from django.db import models
from stdimage import StdImageField, JPEGField
from django.db.models import signals
from django.template.defaultfilters import slugify


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Subcateg(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subcateg = models.ForeignKey(Subcateg, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = StdImageField(
        upload_to='produto_imagens/%Y/%m/', blank=True, null=True, variations={'thumb': (200, 232)})
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco_marketing = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='Preço')
    vezes_sem_juros = models.DecimalField(
        max_digits=2, decimal_places=0)
    preco_marketing_promocional = models.DecimalField(
        max_digits=8, decimal_places=2, default=0, verbose_name='Preço Promo.')

    @property
    def valor_dividido(self):
        return self.preco_marketing/self.vezes_sem_juros

    def __str__(self):
        return self.nome


class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.nome

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'


def save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(save, sender=Produto)
