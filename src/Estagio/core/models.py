from django.db import models


class Conta(models.Model):
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    token = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.email


class Perfil(models.Model):
    conta = models.OneToOneField(Conta, on_delete=models.CASCADE, related_name='perfil')
    nome = models.CharField(max_length=255)
    foto = models.CharField(max_length=500, blank=True)
    bio = models.TextField(blank=True)
    dataNascimento = models.DateField(null=True, blank=True)
    seguindo = models.ManyToManyField('self', symmetrical=False, related_name='seguidores', blank=True)

    def __str__(self):
        return self.nome


class Postagem(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='postagens')
    conteudo = models.TextField()
    dataPublicacao = models.DateTimeField(auto_now_add=True)
    visibilidade = models.BooleanField(default=True)

    class Meta:
        ordering = ['-dataPublicacao']

    def __str__(self):
        return f'{self.perfil.nome} - {self.dataPublicacao:%d/%m/%Y}'


class Interacao(models.Model):
    class Tipo(models.TextChoices):
        CURTIDA = 'CURTIDA', 'Curtida'
        COMENTARIO = 'COMENTARIO', 'Comentário'
        COMPARTILHAMENTO = 'COMPARTILHAMENTO', 'Compartilhamento'

    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE, related_name='interacoes')
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='interacoes')
    tipo = models.CharField(max_length=20, choices=Tipo.choices)
    conteudo = models.TextField(blank=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tipo} - {self.perfil.nome}'


class Mensagem(models.Model):
    remetente = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='mensagens_enviadas')
    destinatario = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='mensagens_recebidas')
    conteudo = models.TextField()
    dataEnvio = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)

    class Meta:
        ordering = ['dataEnvio']

    def __str__(self):
        return f'{self.remetente.nome} -> {self.destinatario.nome}'
