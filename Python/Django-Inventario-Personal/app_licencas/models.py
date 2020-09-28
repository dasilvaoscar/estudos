from django.contrib.auth import get_user_model
from django.db import models
import pandas as pd
User = get_user_model()


class Licenca(models.Model):
    objects = None
    nome = models.CharField(max_length=255)
    usuario = models.ManyToManyField(User, verbose_name='Seleção de Usuário', default=1)
    valor_unitario = models.DecimalField('Valor Unitário em R$', max_digits=15, decimal_places=2, blank=True)

    class Meta:
        verbose_name_plural = "Licenças"

    def __str__(self):
        return self.nome

    def get_usuario(self):
        return '\n'.join([p.username for p in self.usuario.all()])

    def get_quantidade(self):
        user = '\n'.join([p.username for p in self.usuario.all()])
        count = 0
        lista = list(user.split())
        for i in lista:
            count += 1

        return count


class Custo(models.Model):

    licenca = models.ManyToManyField(Licenca)

    def get_licenca(self):
        return ' \n'.join([p.nome for p in self.licenca.all()])

    def get_total_unitario(self):
        tot = 0
        for licenca in self.licenca.all():
            tot += licenca.valor_unitario
            tot = tot * licenca.get_quantidade()

        return 'R$ ' + str(tot).replace(',', '').replace('.', ',')

    class Meta:
        verbose_name_plural = 'Custos Totais'

    def __str__(self):
        return str(self.licenca)