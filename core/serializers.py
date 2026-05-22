from rest_framework import serializers
from .models import (
    Usuario, Estudante, Professor, Coordenador, EmpresaParceira,
    ModeloDocumento, SolicitacaoEstagio, Documento, RelatorioEstagio,
    Pendencia, Notificacao, ValidacaoAutomatica, AnaliseExcecao, Assinatura
)

# Serializers de Usuários
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class CoordenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordenador
        fields = '__all__'

# Serializers de Entidades e Processos
class EmpresaParceiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaParceira
        fields = '__all__'

class ModeloDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloDocumento
        fields = '__all__'

class SolicitacaoEstagioSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitacaoEstagio
        fields = '__all__'

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'

class RelatorioEstagioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatorioEstagio
        fields = '__all__'

# Serializers de Suporte e Controle
class PendenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pendencia
        fields = '__all__'

class NotificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacao
        fields = '__all__'

class ValidacaoAutomaticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValidacaoAutomatica
        fields = '__all__'

class AnaliseExcecaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnaliseExcecao
        fields = '__all__'

class AssinaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assinatura
        fields = '__all__'