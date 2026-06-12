from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioViewSet, EmpresaParceiraViewSet, SupervisorEmpresaViewSet, SolicitacaoEstagioViewSet,
    ModeloDocumentoViewSet, DocumentoViewSet, RelatorioEstagioViewSet, AssinaturaViewSet,
    PendenciaViewSet, AnaliseExcecaoViewSet, NotificacaoViewSet
)

router = DefaultRouter()

router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'empresas', EmpresaParceiraViewSet, basename='empresaparceira')
router.register(r'supervisores', SupervisorEmpresaViewSet, basename='supervisorempresa')
router.register(r'solicitacoes-estagio', SolicitacaoEstagioViewSet, basename='solicitacaoestagio')
router.register(r'modelos-documento', ModeloDocumentoViewSet, basename='modelodocumento')
router.register(r'documentos', DocumentoViewSet, basename='documento')
router.register(r'relatorios-estagio', RelatorioEstagioViewSet, basename='relatorioestagio')
router.register(r'assinaturas', AssinaturaViewSet, basename='assinatura')
router.register(r'pendencias', PendenciaViewSet, basename='pendencia')
router.register(r'analises-excecao', AnaliseExcecaoViewSet, basename='analiseexcecao')
router.register(r'notificacoes', NotificacaoViewSet, basename='notificacao')

urlpatterns = [
    path('', include(router.urls)),
]