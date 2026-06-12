from rest_framework.routers import DefaultRouter

from .views import (
    UsuarioViewSet,
    EmpresaParceiraViewSet,
    SupervisorEmpresaViewSet,
    SolicitacaoEstagioViewSet,
    ModeloDocumentoViewSet,
    DocumentoViewSet,
    RelatorioEstagioViewSet,
    AssinaturaViewSet,
    PendenciaViewSet,
    AnaliseExcecaoViewSet,
    NotificacaoViewSet
)

router = DefaultRouter()

router.register(
    r'usuarios',
    UsuarioViewSet
)

router.register(
    r'empresas',
    EmpresaParceiraViewSet
)

router.register(
    r'supervisores',
    SupervisorEmpresaViewSet
)

router.register(
    r'solicitacoes',
    SolicitacaoEstagioViewSet
)

router.register(
    r'modelos-documento',
    ModeloDocumentoViewSet
)

router.register(
    r'documentos',
    DocumentoViewSet
)

router.register(
    r'relatorios',
    RelatorioEstagioViewSet
)

router.register(
    r'assinaturas',
    AssinaturaViewSet
)

router.register(
    r'pendencias',
    PendenciaViewSet
)

router.register(
    r'analises-excecao',
    AnaliseExcecaoViewSet
)

router.register(
    r'notificacoes',
    NotificacaoViewSet
)

urlpatterns = router.urls