from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import (
    UsuarioViewSet, EstudanteViewSet, ProfessorViewSet, CoordenadorViewSet,
    EmpresaParceiraViewSet, ModeloDocumentoViewSet, SolicitacaoEstagioViewSet,
    DocumentoViewSet, RelatorioEstagioViewSet, PendenciaViewSet,
    NotificacaoViewSet, ValidacaoAutomaticaViewSet, AnaliseExcecaoViewSet,
    AssinaturaViewSet
)

# Criamos o roteador automático da API
router = DefaultRouter()

# Registamos as rotas de cada tabela
router.register(r'usuarios', UsuarioViewSet)
router.register(r'estudantes', EstudanteViewSet)
router.register(r'professores', ProfessorViewSet)
router.register(r'coordenadores', CoordenadorViewSet)
router.register(r'empresas', EmpresaParceiraViewSet)
router.register(r'modelos-documento', ModeloDocumentoViewSet)
router.register(r'solicitacoes-estagio', SolicitacaoEstagioViewSet)
router.register(r'documentos', DocumentoViewSet)
router.register(r'relatorios-estagio', RelatorioEstagioViewSet)
router.register(r'pendencias', PendenciaViewSet)
router.register(r'notificacoes', NotificacaoViewSet)
router.register(r'validacoes-automaticas', ValidacaoAutomaticaViewSet)
router.register(r'analises-excecao', AnaliseExcecaoViewSet)
router.register(r'assinaturas', AssinaturaViewSet)

# Configuração das URLs globais do projeto
urlpatterns = [
    path('admin/', admin.site.urls),
    # Toda vez que alguém aceder a http://localhost:8000/api/, vai entrar na API REST
    path('api/', include(router.urls)), 
]