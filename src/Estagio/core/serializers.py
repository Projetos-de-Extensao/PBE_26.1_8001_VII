from rest_framework import serializers
from .models import Conta, Perfil, Postagem, Interacao, Mensagem


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['id', 'email', 'dataCriacao', 'ativo']
        extra_kwargs = {'senha': {'write_only': True}}


class PerfilSerializer(serializers.ModelSerializer):
    seguindo_count = serializers.SerializerMethodField()
    seguidores_count = serializers.SerializerMethodField()

    class Meta:
        model = Perfil
        fields = ['id', 'conta', 'nome', 'foto', 'bio', 'dataNascimento', 'seguindo_count', 'seguidores_count']

    def get_seguindo_count(self, obj):
        return obj.seguindo.count()

    def get_seguidores_count(self, obj):
        return obj.seguidores.count()


class PostagemSerializer(serializers.ModelSerializer):
    perfil_nome = serializers.CharField(source='perfil.nome', read_only=True)
    total_interacoes = serializers.SerializerMethodField()

    class Meta:
        model = Postagem
        fields = ['id', 'perfil', 'perfil_nome', 'conteudo', 'dataPublicacao', 'visibilidade', 'total_interacoes']
        read_only_fields = ['dataPublicacao']

    def get_total_interacoes(self, obj):
        return obj.interacoes.count()


class InteracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interacao
        fields = ['id', 'postagem', 'perfil', 'tipo', 'conteudo', 'data']
        read_only_fields = ['data']


class MensagemSerializer(serializers.ModelSerializer):
    remetente_nome = serializers.CharField(source='remetente.nome', read_only=True)
    destinatario_nome = serializers.CharField(source='destinatario.nome', read_only=True)

    class Meta:
        model = Mensagem
        fields = ['id', 'remetente', 'remetente_nome', 'destinatario', 'destinatario_nome', 'conteudo', 'dataEnvio', 'lida']
        read_only_fields = ['dataEnvio']
