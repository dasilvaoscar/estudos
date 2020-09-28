from django.db import models
from Core import settings
import os

class ImageUpload(models.Model):
    nome = models.CharField(max_length=255, blank=False)
    descricao = models.TextField(blank=True)
    arquivo = models.FileField(upload_to="images/%d-%m-%Y")
    pub_date = models.DateTimeField('Data de Publicação', auto_now=True)


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Lista de Imagens"

    