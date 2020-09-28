from django.db import models
from django.contrib.auth.models import User


class Tipo(models.Model):
    tipo = models.CharField(max_length=25)

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name_plural = "Tipos"


class Status(models.Model):
    status = models.CharField(max_length=25)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = "Status"


class Modelo(models.Model):
    modelo = models.CharField(max_length=50)

    def __str__(self):
        return self.modelo

    class Meta:
        verbose_name_plural = "Modelos"


class Antivirus(models.Model):
    antivirus = models.CharField(max_length=25)
    versao = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.antivirus

    class Meta:
        verbose_name_plural = "Antí-virus"


class AccessPoint(models.Model):
    nome = models.CharField(max_length=25, verbose_name='Host')
    modelo = models.ForeignKey(Modelo, on_delete=models.SET_NULL, null=True)
    conf = models.FileField(upload_to="ap_conf/%d-%m-%Y")
    mac_address = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Access Points"

    def __str__(self):
        return self.nome


class Camera(models.Model):
    nome = models.CharField(max_length=50)
    ip = models.CharField(max_length=15)
    modelo = models.ForeignKey(Modelo, on_delete=models.SET_NULL, null=True)
    serial = models.IntegerField(blank=True)

    class Meta:
        verbose_name_plural = "Câmeras"

    def __str__(self):
        return self.nome

class Switch(models.Model):
    nome = models.CharField(max_length=25)
    ip = models.CharField(max_length=15)
    modelo = models.ForeignKey(Modelo, on_delete=models.SET_NULL, null=True)
    serial = models.IntegerField(blank=True)

    class Meta:
        verbose_name_plural = "Switches"

    def __str__(self):
        return self.nome


class Computador(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=25)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    tipo = models.ForeignKey(Tipo, default=1, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.SET_NULL, null=True)
    patrimonio = models.IntegerField(blank=True)
    antivirus = models.ForeignKey(Antivirus, on_delete=models.SET_NULL, blank=True, null=True)

    CHOICE = [
        ('L', 'Locado'),
        ('NL', 'Patrimônio')
    ]

    locado = models.CharField(max_length=255, choices=CHOICE)

    class Meta:
        verbose_name_plural = "Computadores"

    def __str__(self):
        return self.nome


class DispositivosDeRede(models.Model):
    nome = models.CharField(max_length=30)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Dispositivos"


class Impressora(models.Model):
    nome = models.CharField(max_length=30)
    ip = models.CharField(max_length=15, blank=True) 
    localizacao = models.CharField(max_length=15, blank=True) 
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Impressoras"
