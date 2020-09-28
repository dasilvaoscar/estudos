from django.db import models


class ATI(models.Model):
    ATI_ID = models.AutoField(primary_key=True)
    CE = models.CharField(verbose_name='Conhecimento', blank=True, max_length=100)
    BL = models.CharField(verbose_name='BL', blank=True, max_length=100)
    REPCNPJ = models.CharField(verbose_name='Repr. CNPJ', blank=True, max_length=100)
    REPREZAO = models.CharField(verbose_name='Repr. Razão Social', blank=True, max_length=100)
    EMISSAO = models.CharField(verbose_name='Data Emissão', blank=True, max_length=100)
    SITUACAO = models.CharField(verbose_name='Situação', blank=True, max_length=100)
    MODALIDADE = models.CharField(verbose_name='Modalidade Frete', blank=True, max_length=100)
    pORIGEM = models.CharField(verbose_name='Porto Origem', blank=True, max_length=100)
    psPROCEDE = models.CharField(verbose_name='Pais Procedência', blank=True, max_length=100)
    UFdestino = models.CharField(verbose_name='UF Destino', blank=True, max_length=100)
    MERCADORIA = models.CharField(verbose_name='Mercadoria', blank=True, max_length=100)



class CNT(models.Model):

    CNT = models.CharField(verbose_name='Conteiner', max_length=100, blank=True, null=True)
    #CNTATI = models.ForeignKey(ATI, on_delete=models.CASCADE, blank=True)
    cntISO = models.CharField(verbose_name='ISO', blank=True, max_length=100)
    cntTipo = models.CharField(verbose_name='Tipo', blank=True, max_length=100)
    cntTara = models.CharField(verbose_name='TARA', blank=True, max_length=100)
    cntPB = models.CharField(verbose_name='Peso Bruto', blank=True, max_length=100)
    m3 = models.CharField(verbose_name='M3', blank=True, max_length=100)
    codIMO = models.CharField(verbose_name='Codigo IMO', blank=True, max_length=100)
    clasIMO = models.CharField(verbose_name='Classe IMO', blank=True, max_length=100)
    ID_CNT = models.ForeignKey(ATI, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.CNT


class Anexos(models.Model):
    ATI_ANEXO = models.ForeignKey(ATI, on_delete=models.CASCADE, blank=True, null=True)
    arquivo = models.FileField(verbose_name="Novos Arquivos", upload_to='media/', blank=True)
    tipo = models.CharField(max_length=6, blank=True)
    data_envio = models.DateTimeField(auto_now_add=True)