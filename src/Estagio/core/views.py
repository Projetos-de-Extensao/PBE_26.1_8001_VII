from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Conta, Perfil, Postagem, Interacao, Mensagem
from .serializers import ContaSerializer, PerfilSerializer, PostagemSerializer, InteracaoSerializer, MensagemSerializer


class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']

    @action(detail=True, methods=['post'])
    def seguir(self, request, pk=None):
        perfil_alvo = self.get_object()
        perfil_seguidor = Perfil.objects.get(conta__id=request.user.id)
        perfil_seguidor.seguindo.add(perfil_alvo)
        return Response({'status': 'seguindo'})

    @action(detail=True, methods=['post'])
    def deixar_de_seguir(self, request, pk=None):
        perfil_alvo = self.get_object()
        perfil_seguidor = Perfil.objects.get(conta__id=request.user.id)
        perfil_seguidor.seguindo.remove(perfil_alvo)
        return Response({'status': 'deixou de seguir'})


class PostagemViewSet(viewsets.ModelViewSet):
    queryset = Postagem.objects.filter(visibilidade=True)
    serializer_class = PostagemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        perfil_id = self.request.query_params.get('perfil')
        if perfil_id:
            queryset = queryset.filter(perfil__id=perfil_id)
        return queryset


class InteracaoViewSet(viewsets.ModelViewSet):
    queryset = Interacao.objects.all()
    serializer_class = InteracaoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        postagem_id = self.request.query_params.get('postagem')
        if postagem_id:
            queryset = queryset.filter(postagem__id=postagem_id)
        return queryset


class MensagemViewSet(viewsets.ModelViewSet):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        perfil_id = self.request.query_params.get('perfil')
        if perfil_id:
            queryset = queryset.filter(
                remetente__id=perfil_id
            ) | queryset.filter(
                destinatario__id=perfil_id
            )
        return queryset
