from django.db import models

# Create your models here.

class LayoutMenssagePresentation(models.Model):
    data = models.DateTimeField('Data da adição', auto_now=True)
    presentation_text = models.TextField(verbose_name='Texto de Apresentação da Aplicação')

    def __str__(self):
        return self.presentation_text

    class Meta:
        verbose_name_plural = "Mensagem do Layout de Apresentação"

class LayoutEmail(models.Model):
    email = models.EmailField(verbose_name='Texto de contato para E-mail')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Mensagem de Apresentação do Email"


class LayoutMenssageContact(models.Model):
    data = models.DateTimeField('Data da adição', auto_now=True)
    fk_layout_presentation = models.ForeignKey('LayoutMenssagePresentation', on_delete=models.SET_NULL, null=True, verbose_name='Menssagem do Layout de Apresentação')
    fk_email_contact = models.ForeignKey('LayoutEmail', verbose_name='Texto de contato para E-mail', on_delete=models.SET_NULL, null=True)
    address_contact_text = models.TextField(verbose_name='Texto de contato para Endereço')
    phone_contact_text = models.TextField(verbose_name='Texto de contato para telefone')

    def __str__(self):
        return str(self.data)

    class Meta:
            verbose_name_plural = "Mensagem do Layout de Contato"