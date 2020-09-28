from django import forms
from .models import *
from django import forms
from .models import *

class RamalForm(forms.ModelForm):
    nome = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': "form-control", 'id': 'successInput'})) 
    ramal = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': "form-control", 'id': 'successInput'})) 
    email = forms.EmailField(widget=forms.EmailInput(attrs={'type': 'email', 'class': 'form-control', 'id': 'email2', 'placeholder': 'Digite o E-mail'}))
    setor = forms.ModelChoiceField(
        queryset=Setor.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'smallSelect'})
        )

    class Meta:
        model = Telefone
        fields = ('nome', 'ramal', 'email', 'setor')


