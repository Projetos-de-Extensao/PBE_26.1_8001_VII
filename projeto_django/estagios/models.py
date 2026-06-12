from django.db import models
from django.contrib.auth.models import AbstractUser


# ==========================
# ENUMS
# ==========================

class TipoUsuario(models.TextChoices):
    ESTUDANTE = "ESTUDANTE", "Estudante"
    PROFESSOR = "PROFESSOR", "Professor"
    COORDENADOR = "COORDENADOR", "Coordenador"


class StatusSolicitacao(models.TextChoices):
    EM_PREENCHIMENTO = "EM_PREENCHIMENTO", "Em preenchimento"
    SUBMETIDA = "SUBMETIDA", "Submetida"
    EM_VALIDACAO = "EM_VALIDACAO", "Em validação"
    COM_PENDENCIAS = "COM_PENDENCIAS", "Com pendências"
    EM_ANALISE_EXCECAO = "EM_ANALISE_EXCECAO", "Em análise de exceção"
    APROVADA = "APROVADA", "Aprovada"
    REPROVADA = "REPROVADA", "Reprovada"


class TipoDocumento(models.TextChoices):
    CONTRATO = "CONTRATO", "Contrato"
    TERMO_COMPROMISSO = "TERMO_COMPROMISSO", "Termo de Compromisso"
    RELATORIO_PARCIAL = "RELATORIO_PARCIAL", "Relatório Parcial"
    RELATORIO_FINAL = "RELATORIO_FINAL", "Relatório Final"
    APOLICE_SEGURO = "APOLICE_SEGURO", "Apólice de Seguro"
    OUTRO = "OUTRO", "Outro"


class StatusDocumento(models.TextChoices):
    ENVIADO = "ENVIADO", "Enviado"
    VALIDADO = "VALIDADO", "Validado"
    COM_PENDENCIA = "COM_PENDENCIA", "Com Pendência"
    REJEITADO = "REJEITADO", "Rejeitado"
    ASSINADO = "ASSINADO", "Assinado"


class TipoPendencia(models.TextChoices):
    DADO_AUSENTE = "DADO_AUSENTE", "Dado Ausente"
    ASSINATURA_FALTANTE = "ASSINATURA_FALTANTE", "Assinatura Faltante"
    DOCUMENTO_INVALIDO = "DOCUMENTO_INVALIDO", "Documento Inválido"
    INCONSISTENCIA_LEGAL = "INCONSISTENCIA_LEGAL", "Inconsistência Legal"
    INCONSISTENCIA_INSTITUCIONAL = "INCONSISTENCIA_INSTITUCIONAL", "Inconsistência Institucional"


class TipoNotificacao(models.TextChoices):
    STATUS_ALTERADO = "STATUS_ALTERADO", "Status Alterado"
    PENDENCIA_IDENTIFICADA = "PENDENCIA_IDENTIFICADA", "Pendência Identificada"
    PRAZO_PROXIMO = "PRAZO_PROXIMO", "Prazo Próximo"
    DOCUMENTO_ASSINADO = "DOCUMENTO_ASSINADO", "Documento Assinado"


class DecisaoCoordenacao(models.TextChoices):
    APROVAR_EXCECAO = "APROVAR_EXCECAO", "Aprovar Exceção"
    SOLICITAR_AJUSTE = "SOLICITAR_AJUSTE", "Solicitar Ajuste"
    REPROVAR = "REPROVAR", "Reprovar"


# ==========================
# USUARIO
# ==========================

class Usuario(AbstractUser):

    email = models.EmailField(unique=True)

    tipo = models.CharField(
        max_length=20,
        choices=TipoUsuario.choices
    )

    ativo = models.BooleanField(default=True)

    matricula = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    curso = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    periodo = models.IntegerField(
        blank=True,
        null=True
    )

    area_atuacao = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    setor = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.get_full_name() or self.email


# ==========================
# EMPRESA
# ==========================

class EmpresaParceira(models.Model):

    razao_social = models.CharField(max_length=200)

    cnpj = models.CharField(
        max_length=18,
        unique=True
    )

    responsavel_legal = models.CharField(
        max_length=150
    )

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.razao_social


class SupervisorEmpresa(models.Model):

    empresa = models.ForeignKey(
        EmpresaParceira,
        on_delete=models.CASCADE,
        related_name="supervisores"
    )

    nome = models.CharField(max_length=150)

    email = models.EmailField()

    cargo = models.CharField(max_length=100)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


# ==========================
# SOLICITACAO
# ==========================

class SolicitacaoEstagio(models.Model):

    estudante = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="solicitacoes_estudante"
    )

    professor = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="solicitacoes_professor"
    )

    empresa = models.ForeignKey(
        EmpresaParceira,
        on_delete=models.CASCADE,
        related_name="solicitacoes"
    )

    supervisor = models.ForeignKey(
        SupervisorEmpresa,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=30,
        choices=StatusSolicitacao.choices,
        default=StatusSolicitacao.EM_PREENCHIMENTO
    )

    score_conformidade = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    criado_em = models.DateTimeField(auto_now_add=True)

    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Solicitação #{self.id}"


# ==========================
# MODELO DOCUMENTO
# ==========================

class ModeloDocumento(models.Model):

    nome = models.CharField(max_length=100)

    versao = models.CharField(max_length=20)

    descricao = models.TextField(blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


# ==========================
# DOCUMENTO
# ==========================

class Documento(models.Model):

    solicitacao = models.ForeignKey(
        SolicitacaoEstagio,
        on_delete=models.CASCADE,
        related_name="documentos"
    )

    modelo = models.ForeignKey(
        ModeloDocumento,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    nome_arquivo = models.CharField(max_length=255)

    arquivo = models.FileField(
        upload_to="documentos/"
    )

    tipo = models.CharField(
        max_length=30,
        choices=TipoDocumento.choices
    )

    status = models.CharField(
        max_length=30,
        choices=StatusDocumento.choices,
        default=StatusDocumento.ENVIADO
    )

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_arquivo


# ==========================
# RELATORIO
# ==========================

class RelatorioEstagio(models.Model):

    solicitacao = models.OneToOneField(
        SolicitacaoEstagio,
        on_delete=models.CASCADE,
        related_name="relatorio"
    )

    professor = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True
    )

    titulo = models.CharField(max_length=200)

    descricao = models.TextField()


    aprovado = models.BooleanField(
        default=False
    )



# ==========================
# ASSINATURA
# ==========================

class Assinatura(models.Model):

    documento = models.ForeignKey(
        Documento,
        on_delete=models.CASCADE,
        related_name="assinaturas"
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )

    hash_assinatura = models.CharField(
        max_length=255
    )

    data_assinatura = models.DateTimeField(
        auto_now_add=True
    )


# ==========================
# PENDENCIA
# ==========================

class Pendencia(models.Model):

    solicitacao = models.ForeignKey(
        SolicitacaoEstagio,
        on_delete=models.CASCADE,
        related_name="pendencias"
    )

    tipo = models.CharField(
        max_length=50,
        choices=TipoPendencia.choices
    )

    descricao = models.TextField()

    resolvida = models.BooleanField(
        default=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )


# ==========================
# ANALISE EXCECAO
# ==========================

class AnaliseExcecao(models.Model):

    solicitacao = models.OneToOneField(
        SolicitacaoEstagio,
        on_delete=models.CASCADE,
        related_name="analise_excecao"
    )

    coordenador = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True
    )

    justificativa = models.TextField()

    decisao = models.CharField(
        max_length=30,
        choices=DecisaoCoordenacao.choices
    )

    data_analise = models.DateTimeField(
        auto_now_add=True
    )


# ==========================
# NOTIFICACAO
# ==========================

class Notificacao(models.Model):

    solicitacao = models.ForeignKey(
        SolicitacaoEstagio,
        on_delete=models.CASCADE,
        related_name="notificacoes"
    )

    destinatario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="notificacoes"
    )

    tipo = models.CharField(
        max_length=50,
        choices=TipoNotificacao.choices
    )

    mensagem = models.TextField()

    lida = models.BooleanField(
        default=False
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )
