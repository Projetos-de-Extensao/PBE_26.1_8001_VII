from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import SolicitacaoEstagio
from .serializers import SolicitacaoEstagioSerializer

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

from .serializers import (
    UsuarioSerializer,
    EmpresaParceiraSerializer,
    SupervisorEmpresaSerializer,
    SolicitacaoEstagioSerializer,
    ModeloDocumentoSerializer,
    DocumentoSerializer,
    RelatorioEstagioSerializer,
    AssinaturaSerializer,
    PendenciaSerializer,
    AnaliseExcecaoSerializer,
    NotificacaoSerializer
)

from .services.validacao import validar_solicitacao


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.filter(tipo="ESTUDANTE")
    serializer_class = UsuarioSerializer


class EmpresaParceiraViewSet(ModelViewSet):
    queryset = EmpresaParceira.objects.all()
    serializer_class = EmpresaParceiraSerializer


class SupervisorEmpresaViewSet(ModelViewSet):
    queryset = SupervisorEmpresa.objects.all()
    serializer_class = SupervisorEmpresaSerializer


class SolicitacaoEstagioViewSet(ModelViewSet):
    queryset = SolicitacaoEstagio.objects.all()
    serializer_class = SolicitacaoEstagioSerializer

    # 🔥 AGORA USANDO SEU ROBÔ OFICIAL:
    def perform_create(self, serializer):
        # 1. O Django salva a solicitação e cria os 3 Documentos no banco
        solicitacao = serializer.save()

        # 2. Chamamos a SUA função do service que valida extensões e regras reais
        validar_solicitacao(solicitacao)

        # 3. Atualizamos a memória do Django com o resultado do seu robô
        solicitacao.refresh_from_db()


class ModeloDocumentoViewSet(ModelViewSet):
    queryset = ModeloDocumento.objects.all()
    serializer_class = ModeloDocumentoSerializer


class DocumentoViewSet(ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer


class RelatorioEstagioViewSet(ModelViewSet):
    queryset = RelatorioEstagio.objects.all()
    serializer_class = RelatorioEstagioSerializer


class AssinaturaViewSet(ModelViewSet):
    queryset = Assinatura.objects.all()
    serializer_class = AssinaturaSerializer


class PendenciaViewSet(ModelViewSet):
    queryset = Pendencia.objects.all()
    serializer_class = PendenciaSerializer


class AnaliseExcecaoViewSet(ModelViewSet):
    queryset = AnaliseExcecao.objects.all()
    serializer_class = AnaliseExcecaoSerializer


class NotificacaoViewSet(ModelViewSet):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer