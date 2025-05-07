from rest_framework import serializers
from .models import *

class PessoaSerializer(serializers.ModelSerializer):
    sexo = serializers.CharField(source='get_sexo_display')
    raca_cor = serializers.CharField(source='get_raca_cor_display')
    
    class Meta:
        model = Pessoa
        fields = '__all__'
        read_only_fields = ('id',)

class DomicilioSerializer(serializers.ModelSerializer):
    tipo_esgoto = serializers.CharField(source='get_tipo_esgoto_display')
    pessoas = PessoaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Domicilio
        fields = '__all__'

class EntrevistaSerializer(serializers.ModelSerializer):
    domicilio = DomicilioSerializer()
    entrevistador = serializers.StringRelatedField()
    
    class Meta:
        model = Entrevista
        fields = '__all__'
        depth = 1

class RelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relatorio
        fields = '__all__'

class EntrevistadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrevistador
        fields = ['id', 'matricula', 'nome', 'area_cobertura']

# E no EntrevistaSerializer manter:
entrevistador = serializers.StringRelatedField() 