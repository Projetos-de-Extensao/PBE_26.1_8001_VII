from rest_framework.routers import DefaultRouter
from .views import ContaViewSet, PerfilViewSet, PostagemViewSet, InteracaoViewSet, MensagemViewSet

router = DefaultRouter()
router.register(r'contas', ContaViewSet)
router.register(r'perfis', PerfilViewSet)
router.register(r'postagens', PostagemViewSet)
router.register(r'interacoes', InteracaoViewSet)
router.register(r'mensagens', MensagemViewSet)

urlpatterns = router.urls
