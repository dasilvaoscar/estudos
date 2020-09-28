from django import forms
from .models import *

class CardapioForm(forms.ModelForm):
    nome = forms.CharField(label='Nome da Imagem', max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'id': 'successInput'})) 
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", 'id': 'comment', 'rows': '7'}))

    class Meta:
        model = ImageUpload
        fields = ('nome', 'descricao', 'arquivo')
        readonly_fields=('pub_date',)
        widgets = { 
            'arquivo': forms.FileInput(attrs={'class': 'form-control', 'multiple': True}),
        }

