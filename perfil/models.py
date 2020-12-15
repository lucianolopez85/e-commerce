from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User

import re
from utils.validacpf import valida_cpf


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,
                                   verbose_name='Usuário')
    idade = models.PositiveIntegerField()
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.usuario}'

    def clean(self):
        error_messages = {}

        cpf_enviado = self.cpf or None
        cpf_salvo = None
        perfil = Perfil.objects.filter(cpf=cpf_enviado).first()

        if perfil:
            cpf_salvo = perfil.cpf

            if cpf_salvo is not None and self.pk != perfil.pk:
                error_messages['cpf'] = 'CPF já existe.'

        if not valida_cpf(self.cpf):
            error_messages['cpf'] = 'Digite um CPF válido'

        if re.search(r'[^0-9]', self.cep) or len(self.cep) < 8:
            error_messages['cep'] = 'CEP inválido, digite os 8 digitos do CEP.'

        if error_messages:
            raise ValidationError(error_messages)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class Contato (models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    cel = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.cel} {self.perfil}'

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'


class Endereco(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=50, default='Endereço principal')
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(
        default="SP",
        max_length=2,
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )

    def __str__(self):
        return f'{self.descricao} - {self.perfil}'

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
