from django import forms
from .models import *
from django import forms
from .models import *
from django.contrib.auth.models import User

class ComputadorForm(forms.ModelForm):
    nome = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': "form-control", 'id': 'successInput'})) 
    usuario = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'smallSelect'})
        )
    tipo = forms.ModelChoiceField(
        queryset=Tipo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'smallSelect'})
        )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'smallSelect'})
        )
    modelo = forms.ModelChoiceField(
        queryset=Modelo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'smallSelect'})
        )
    patrimonio =  forms.IntegerField(
        widget=forms.TextInput(attrs={'class': "form-control", 'id': 'successInput'})
        )
    antivirus = forms.ModelChoiceField(
        queryset=Antivirus.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'smallSelect'})
        )

    CHOICE = [
        ('L', 'Locado'),
        ('NL', 'Patrimônio')
    ]

    locado = forms.ChoiceField(
        choices=CHOICE,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'smallSelect'})
        )

    class Meta:
        model = Computador
        fields = ('nome', 'usuario', 'tipo', 'status',
                 'modelo', 'patrimonio', 'antivirus', 'locado')
        
class ApForm(forms.ModelForm):
    nome = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': "form-control", 'id': 'successInput'})) 
    modelo = forms.ModelChoiceField(
        queryset=Modelo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'smallSelect'})
        )
        
    mac_address = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': "form-control", 'id': 'successInput'}))

    class Meta:
        model = AccessPoint
        fields = ('nome', 'modelo', 'conf', 'mac_address',)
        widgets = { 
            'conf': forms.FileInput(attrs={'class': 'form-control', 'multiple': True}),
        }


class AntivirusForm(forms.ModelForm):
    antivirus = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': "form-control", 'id': 'successInput'})) 
    versao = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': "form-control", 'id': 'successInput'}))

    class Meta:
        model = Antivirus
        fields = ('antivirus', 'versao')
        

class CameraForm(forms.ModelForm):
    nome = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': "form-control", 'id': 'successInput'})) 
    modelo = forms.ModelChoiceField(
        queryset=Modelo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'smallSelect'})
        )
        
    serial = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'id': 'successInput'}))
    ip = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': "form-control", 'id': 'successInput'}))

    class Meta:
        model = Camera
        fields = ('nome', 'modelo', 'serial', 'ip',)


class SwitchForm(forms.ModelForm):
    nome = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': "form-control", 'id': 'successInput'})) 
    modelo = forms.ModelChoiceField(
        queryset=Modelo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'smallSelect'})
        )
        
    serial = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'id': 'successInput'}))
    ip = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': "form-control", 'id': 'successInput'}))

    class Meta:
        model = Switch
        fields = ('nome', 'modelo', 'serial', 'ip',)


class ImpressorasForm(forms.ModelForm):
    nome = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': "form-control", 'id': 'successInput'})) 
    modelo = forms.ModelChoiceField(
        queryset=Modelo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'smallSelect'})
        )    
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'smallSelect'})
        )
    ip = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': "form-control", 'id': 'successInput'}))

    class Meta:
        model = Impressora
        fields = ('nome', 'modelo', 'status', 'ip')


class DDRForm(forms.ModelForm):
    nome = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': "form-control", 'id': 'successInput'})) 
    modelo = forms.ModelChoiceField(
        queryset=Modelo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'smallSelect'})
        )    
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'smallSelect'})
        )
    tipo = forms.ModelChoiceField(
        queryset=Tipo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'smallSelect'})
        )

    class Meta:
        model = DispositivosDeRede
        fields = ('nome', 'modelo', 'status', 'tipo')