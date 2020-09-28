from django.db import models


class Setor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Setores"


class Telefone(models.Model):

    nome = models.CharField(max_length=25)
    ramal = models.CharField(max_length=12)
    email = models.EmailField(max_length=70, blank=True)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Telefones"
