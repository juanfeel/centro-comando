from django import forms
from .models import NodoServidor, IncidenciaServidor

class NodoServidorForm(forms.ModelForm):
    class Meta:
        model = NodoServidor
        fields = ['nombre_host', 'direccion_ip', 'motor_contenedores', 'proxy_inverso', 'en_produccion']
        widgets = {
            'nombre_host': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_ip': forms.TextInput(attrs={'class': 'form-control'}),
            'motor_contenedores': forms.Select(attrs={'class': 'form-select'}),
            'proxy_inverso': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'en_produccion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class IncidenciaServidorForm(forms.ModelForm):
    class Meta:
        model = IncidenciaServidor
        fields = ['titulo', 'descripcion', 'severidad']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': 3
            }),
            'severidad': forms.Select(attrs={'class': 'form-select'}),
        }