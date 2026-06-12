from rest_framework import viewsets
from .models import (
    Usuario, EmpresaParceira, SupervisorEmpresa, SolicitacaoEstagio,
    ModeloDocumento, Documento, RelatorioEstagio, Assinatura, Pendencia,
    AnaliseExcecao, Notificacao
)
from .serializers import (
    UsuarioSerializer, EmpresaParceiraSerializer, SupervisorEmpresaSerializer,
    SolicitacaoEstagioSerializer, ModeloDocumentoSerializer, DocumentoSerializer,
    RelatorioEstagioSerializer, AssinaturaSerializer, PendenciaSerializer,
    AnaliseExcecaoSerializer, NotificacaoSerializer
)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EmpresaParceiraViewSet(viewsets.ModelViewSet):
    queryset = EmpresaParceira.objects.all()
    serializer_class = EmpresaParceiraSerializer

class SupervisorEmpresaViewSet(viewsets.ModelViewSet):
    queryset = SupervisorEmpresa.objects.all()
    serializer_class = SupervisorEmpresaSerializer

class SolicitacaoEstagioViewSet(viewsets.ModelViewSet):
    queryset = SolicitacaoEstagio.objects.all()
    serializer_class = SolicitacaoEstagioSerializer

class ModeloDocumentoViewSet(viewsets.ModelViewSet):
    queryset = ModeloDocumento.objects.all()
    serializer_class = ModeloDocumentoSerializer

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

class RelatorioEstagioViewSet(viewsets.ModelViewSet):
    queryset = RelatorioEstagio.objects.all()
    serializer_class = RelatorioEstagioSerializer

class AssinaturaViewSet(viewsets.ModelViewSet):
    queryset = Assinatura.objects.all()
    serializer_class = AssinaturaSerializer

class PendenciaViewSet(viewsets.ModelViewSet):
    queryset = Pendencia.objects.all()
    serializer_class = PendenciaSerializer

class AnaliseExcecaoViewSet(viewsets.ModelViewSet):
    queryset = AnaliseExcecao.objects.all()
    serializer_class = AnaliseExcecaoSerializer

class NotificacaoViewSet(viewsets.ModelViewSet):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer