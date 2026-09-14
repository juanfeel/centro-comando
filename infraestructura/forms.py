from django import forms
from .models import NodoServidor, IncidenciaServidor, MantenimientoNodo

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


class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = MantenimientoNodo
        fields = ['servidor', 'titulo_tarea', 'descripcion_tecnica', 'tipo',
        'fecha_programada', 'completado']
        widgets = {
            'servidor': forms.Select(attrs={'class': 'form-select'}),
            'titulo_tarea': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_tecnica': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'fecha_programada': forms.DateTimeInput(attrs={'class': 'form-control', 'type':
            'datetime-local'}),
            'completado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }