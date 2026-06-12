from rest_framework import serializers
from .models import (
    Usuario,
    EmpresaParceira,
    SupervisorEmpresa,
    SolicitacaoEstagio,
    ModeloDocumento,
    Documento,
    RelatorioEstagio,
    Assinatura,
    Pendencia,
    AnaliseExcecao,
    Notificacao
)
from django.utils import timezone

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ["password", "groups", "user_permissions"]


class EmpresaParceiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaParceira
        fields = "__all__"


class SupervisorEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupervisorEmpresa
        fields = "__all__"


class SolicitacaoEstagioSerializer(serializers.ModelSerializer):
    # Adicionamos o 'label' para customizar o texto que aparece na tela
    upload_contrato = serializers.FileField(
        write_only=True, 
        required=True,
        label="Contrato de Estágio (PDF)"
    )
    upload_termo = serializers.FileField(
        write_only=True, 
        required=True,
        label="Termo de Compromisso de Estágio (PDF)"
    )
    upload_apolice = serializers.FileField(
        write_only=True, 
        required=True,
        label="Apólice de Seguro de Acidentes Pessoais (PDF)"
    )

    class Meta:
        model = SolicitacaoEstagio
        fields = "__all__"

        read_only_fields = [
            "estudante",
            "supervisor",
            "professor",
            "criado_em",
            "atualizado_em"
        ]
    def create(self, validated_data):
        # 1. Removemos os arquivos dos dados validados da solicitação
        arquivo_contrato = validated_data.pop("upload_contrato")
        arquivo_termo = validated_data.pop("upload_termo")
        arquivo_apolice = validated_data.pop("upload_apolice")

        # 🔥 AQUI ESTÁ O TRUQUE PARA O MVP:
        # Substitua o número abaixo pelo ID REAL do Aluno que você criou no seu Admin
        validated_data["estudante_id"] = 3  

        # 2. Criamos a Solicitação de Estágio normalmente
        solicitacao = super().create(validated_data)

        # 3. Criamos automaticamente os 3 registros na tabela Documento
        Documento.objects.create(
            solicitacao=solicitacao,
            tipo="CONTRATO",
            nome_arquivo=arquivo_contrato.name,
            arquivo=arquivo_contrato
        )
        Documento.objects.create(
            solicitacao=solicitacao,
            tipo="TERMO_COMPROMISSO",
            nome_arquivo=arquivo_termo.name,
            arquivo=arquivo_termo
        )
        Documento.objects.create(
            solicitacao=solicitacao,
            tipo="APOLICE_SEGURO",
            nome_arquivo=arquivo_apolice.name,
            arquivo=arquivo_apolice
        )

        return solicitacao
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # 🔥 TRUQUE DE SEGURANÇA:
        # Se for um POST (Criação de nova solicitação), o status fica estritamente como Leitura.
        # O Aluno não consegue mexer e o banco usará o valor padrão (Em preenchimento).
        request = self.context.get("request")
        if request and request.method == "POST":
            self.fields["status"].read_only = True
            self.fields["score_conformidade"].read_only = True

class ModeloDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloDocumento
        fields = "__all__"


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = "__all__"


class RelatorioEstagioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatorioEstagio
        fields = "__all__"
        # ✂️ Tiramos a 'data_entrega' daqui
        read_only_fields = ["aprovado", "professor", "solicitacao"]

    def create(self, validated_data):
        id_estudante_logado = 3 
        
        solicitacao_ativa = SolicitacaoEstagio.objects.filter(
            estudante_id=id_estudante_logado
        ).order_by('-id').first()
        
        if not solicitacao_ativa:
            raise serializers.ValidationError(
                {"error": "Este aluno não possui nenhuma solicitação de estágio ativa."}
            )
        
        validated_data["solicitacao"] = solicitacao_ativa
        return super().create(validated_data)

class AssinaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assinatura
        fields = "__all__"


class PendenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pendencia
        fields = "__all__"


class AnaliseExcecaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnaliseExcecao
        fields = "__all__"


class NotificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacao
        fields = "__all__"