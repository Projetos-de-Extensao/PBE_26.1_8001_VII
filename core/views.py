from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    Usuario, Estudante, Professor, Coordenador, EmpresaParceira,
    ModeloDocumento, SolicitacaoEstagio, Documento, RelatorioEstagio,
    Pendencia, Notificacao, ValidacaoAutomatica, AnaliseExcecao, Assinatura
)
from .serializers import (
    UsuarioSerializer, EstudanteSerializer, ProfessorSerializer, CoordenadorSerializer,
    EmpresaParceiraSerializer, ModeloDocumentoSerializer, SolicitacaoEstagioSerializer,
    DocumentoSerializer, RelatorioEstagioSerializer, PendenciaSerializer,
    NotificacaoSerializer, ValidacaoAutomaticaSerializer, AnaliseExcecaoSerializer,
    AssinaturaSerializer
)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class CoordenadorViewSet(viewsets.ModelViewSet):
    queryset = Coordenador.objects.all()
    serializer_class = CoordenadorSerializer

class EmpresaParceiraViewSet(viewsets.ModelViewSet):
    queryset = EmpresaParceira.objects.all()
    serializer_class = EmpresaParceiraSerializer

class ModeloDocumentoViewSet(viewsets.ModelViewSet):
    queryset = ModeloDocumento.objects.all()
    serializer_class = ModeloDocumentoSerializer

class SolicitacaoEstagioViewSet(viewsets.ModelViewSet):
    queryset = SolicitacaoEstagio.objects.all()
    serializer_class = SolicitacaoEstagioSerializer

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

class RelatorioEstagioViewSet(viewsets.ModelViewSet):
    queryset = RelatorioEstagio.objects.all()
    serializer_class = RelatorioEstagioSerializer

class PendenciaViewSet(viewsets.ModelViewSet):
    queryset = Pendencia.objects.all()
    serializer_class = PendenciaSerializer

class NotificacaoViewSet(viewsets.ModelViewSet):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer

class ValidacaoAutomaticaViewSet(viewsets.ModelViewSet):
    queryset = ValidacaoAutomatica.objects.all()
    serializer_class = ValidacaoAutomaticaSerializer

class AnaliseExcecaoViewSet(viewsets.ModelViewSet):
    queryset = AnaliseExcecao.objects.all()
    serializer_class = AnaliseExcecaoSerializer

class AssinaturaViewSet(viewsets.ModelViewSet):
    queryset = Assinatura.objects.all()
    serializer_class = AssinaturaSerializer