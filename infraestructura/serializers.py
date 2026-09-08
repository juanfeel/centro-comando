from rest_framework import serializers
from .models import NodoServidor, RegistroAuditoria, IncidenciaServidor

class NodoServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodoServidor
        fields = '__all__'

class RegistroAuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroAuditoria
        fields = '__all__'

class IncidenciaServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidenciaServidor
        fields = '__all__'