from django import forms
from django.forms import formset_factory, CharField, inlineformset_factory

#from .models import Post
from Cadastro.models import ATI, CNT, Anexos


class MercForm(forms.ModelForm):

    class Meta:
        model = CNT
        exclude = ('ID_CNT', 'ATI_ID', 'MERCADORIA')
        widgets = {
            'CNT': forms.TextInput(attrs={'class': 'form-control input-border-bottom'}),
            'cntISO': forms.TextInput(attrs={'class': 'form-control input-border-bottom'}),
            'cntTipo': forms.TextInput(attrs={'class': 'form-control input-border-bottom'}),
            'cntTara': forms.TextInput(attrs={'class': 'form-control input-border-bottom'}),
            'cntPB': forms.TextInput(attrs={'class': 'form-control input-border-bottom'}),
            'm3': forms.TextInput(attrs={'class': 'form-control input-border-bottom'}),
            'codIMO': forms.TextInput(attrs={'class': 'form-control input-border-bottom'}),
            'clasIMO': forms.TextInput(attrs={'class': 'form-control input-border-bottom'}),
        }

class ATIForm(forms.ModelForm):

    class Meta:
        model = ATI
        #exclude = ('emissao', 'situacao', 'modalidade', 'pOrigem', 'psProcede', 'UFdestino')
        exclude = ()

        widgets = {
            'CE': forms.TextInput(attrs={'class': 'form-control input-full'}),
            'BL': forms.TextInput(attrs={'class': 'form-control input-full'}),
            'REPCNPJ': forms.TextInput(attrs={'class': 'form-control input-full'}),
            'REPREZAO': forms.TextInput(attrs={'class': 'form-control input-full'}),
            'EMISSAO': forms.TextInput(attrs={'class': 'form-control input-full'}),
            'SITUACAO': forms.TextInput(attrs={'class': 'form-control input-full'}),
            'MODALIDADE': forms.TextInput(attrs={'class': 'form-control input-full'}),
            'pORIGEM': forms.TextInput(attrs={'class': 'form-control input-full'}),
            'psPROCEDE': forms.TextInput(attrs={'class': 'form-control input-full'}),
            'UFdestino': forms.TextInput(attrs={'class': 'form-control input-full'})
        }


class AnexoForm(forms.ModelForm):
    class Meta:
        model = Anexos
        readonly_fields=('data_envio', )
        fields = ('arquivo',)
        widgets = {
            'arquivo': forms.FileInput(attrs={'class': 'form-control', 'multiple': True}),
            #'arquivo' : forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True})),
            'data_envio': forms.DateTimeField,
        }




"""
class StatusForm(forms.ModelForm):

    class Meta:
        model = ATI
        fields = ('EMISSAO', 'SITUACAO', 'MODALIDADE', 'pORIGEM', 'psPROCEDE', 'UFdestino')
        widgets = {
            'EMISSAO': forms.TextInput(attrs={'class': 'form-control'}),
            'SITUACAO': forms.TextInput(attrs={'class': 'form-control'}),
            'MODALIDADE': forms.TextInput(attrs={'class': 'form-control'}),
            'pORIGEM': forms.TextInput(attrs={'class': 'form-control'}),
            'psPROCEDE': forms.TextInput(attrs={'class': 'form-control'}),
            'UFdestino': forms.TextInput(attrs={'class': 'form-control'})
        }"""
