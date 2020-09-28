from django.db import models
from sqlalchemy import create_engine
import pandas as pd


class Empresas(models.Model):
    nome = models.CharField('Nome', max_length=50)

    def get_total(self):
        tot = 0
        for valor in Contrato.objects.all():
            tot += valor.valor_contrato

            return tot

    get_total.short_description = 'Total'

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Lançamento'


class FormaPagamento(models.Model):
    pagamento = models.CharField('Forma de Pagamento', max_length=40)

    def __str__(self):
        return self.pagamento

    class Meta:
        verbose_name_plural = "Formas de Pagamento"


class Contrato(models.Model):
    PAGAMENTO = (
        ('ME', 'Mensal'),
        ('AN', 'Anual'),
    )

    t_empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE, verbose_name='Empresa')
    servico = models.CharField('Serviço', max_length=50)
    forma_de_pagamento = models.ForeignKey(FormaPagamento, verbose_name='Forma de Pagamento', on_delete=models.SET_NULL, null=True)
    dt_lancamento = models.DateField('Data de Lançamento')
    valor_contrato = models.DecimalField('Valor', max_digits=15, decimal_places=2)

    def __str__(self):
        return self.servico

    class Meta:
        verbose_name_plural = "Contratos de Serviço"

