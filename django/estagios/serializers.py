from rest_framework import serializers
from .models import (
    Usuario, EmpresaParceira, SupervisorEmpresa, SolicitacaoEstagio,
    ModeloDocumento, Documento, RelatorioEstagio, Assinatura, Pendencia,
    AnaliseExcecao, Notificacao
)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class EmpresaParceiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaParceira
        fields = '__all__'

class SupervisorEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupervisorEmpresa
        fields = '__all__'

class SolicitacaoEstagioSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitacaoEstagio
        fields = '__all__'

class ModeloDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloDocumento
        fields = '__all__'

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'

class RelatorioEstagioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatorioEstagio
        fields = '__all__'

class AssinaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assinatura
        fields = '__all__'

class PendenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pendencia
        fields = '__all__'

class AnaliseExcecaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnaliseExcecao
        fields = '__all__'

class NotificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacao
        fields = '__all__'