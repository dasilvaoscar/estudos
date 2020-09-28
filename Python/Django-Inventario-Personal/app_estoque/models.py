from django.db import models

# Create your models here.

class Estoque(models.Model):  

    equipamento = models.CharField(max_length=50, verbose_name='Equipametos')
    descricao = models.TextField(max_length=300, verbose_name='Descrição')
    quantidade = models.IntegerField('Quantidade')

    class Meta:
        verbose_name_plural = "Estoque de TI"

    def __str__(self):
        return self.equipamento
    


        