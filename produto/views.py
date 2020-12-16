from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from. import models


class ListaProdutos(ListView):
    model = models.Produto
    # template_name = 'produto/lista.html'   #aqui nomeia o html com o nome que preferir


class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('DetalheProduto')


class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('AdicionarAoCarrinho')


class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('RemoverDoCarrinho')


class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')
