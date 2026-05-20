from django.db import models

# ==============================================================================
# 1. ENUMERAÇÕES (Choices)
# ==============================================================================

class StatusSolicitacao(models.TextChoices):
    EM_PREENCHIMENTO = 'EM_PREENCHIMENTO', 'Em Preenchimento'
    SUBMETIDA = 'SUBMETIDA', 'Submetida'
    EM_VALIDACAO = 'EM_VALIDACAO', 'Em Validação'
    COM_PENDENCIAS = 'COM_PENDENCIAS', 'Com Pendências'
    EM_ANALISE_EXCECAO = 'EM_ANALISE_EXCECAO', 'Em Análise de Exceção'
    APROVADA = 'APROVADA', 'Aprovada'
    REPROVADA = 'REPROVADA', 'Reprovada'

class TipoDocumento(models.TextChoices):
    CONTRATO = 'CONTRATO', 'Contrato'
    TERMO_COMPROMISSO = 'TERMO_COMPROMISSO', 'Termo de Compromisso'
    RELATORIO_PARCIAL = 'RELATORIO_PARCIAL', 'Relatório Parcial'
    RELATORIO_FINAL = 'RELATORIO_FINAL', 'Relatório Final'
    APOLICE_SEGURO = 'APOLICE_SEGURO', 'Apólice de Seguro'
    OUTRO = 'OUTRO', 'Outro'

class StatusDocumento(models.TextChoices):
    ENVIADO = 'ENVIADO', 'Enviado'
    VALIDADO = 'VALIDADO', 'Validado'
    COM_PENDENCIA = 'COM_PENDENCIA', 'Com Pendência'
    REJEITADO = 'REJEITADO', 'Rejeitado'
    ASSINADO = 'ASSINADO', 'Assinado'

class TipoNotificacao(models.TextChoices):
    STATUS_ALTERADO = 'STATUS_ALTERADO', 'Status Alterado'
    PENDENCIA_IDENTIFICADA = 'PENDENCIA_IDENTIFICADA', 'Pendência Identificada'
    PRAZO_PROXIMO = 'PRAZO_PROXIMO', 'Prazo Próximo'
    DOCUMENTO_ASSINADO = 'DOCUMENTO_ASSINADO', 'Documento Assinado'

class TipoPendencia(models.TextChoices):
    DADO_AUSENTE = 'DADO_AUSENTE', 'Dado Ausente'
    ASSINATURA_FALTANTE = 'ASSINATURA_FALTANTE', 'Assinatura Faltante'
    DOCUMENTO_INVALIDO = 'DOCUMENTO_INVALIDO', 'Documento Inválido'
    INCONSISTENCIA_LEGAL = 'INCONSISTENCIA_LEGAL', 'Inconsistência Legal'
    INCONSISTENCIA_INSTITUCIONAL = 'INCONSISTENCIA_INSTITUCIONAL', 'Inconsistência Institucional'

class DecisaoCoordenacao(models.TextChoices):
    APROVAR_EXCECAO = 'APROVAR_EXCECAO', 'Aprovar Exceção'
    SOLICITAR_AJUSTE = 'SOLICITAR_AJUSTE', 'Solicitar Ajuste'
    REPROVAR = 'REPROVAR', 'Reprovar'

# ==============================================================================
# 2. MODELOS DE USUÁRIOS E HERANÇA
# ==============================================================================

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email_institucional = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Estudante(Usuario):
    matricula = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)
    periodo = models.IntegerField()

class Professor(Usuario):
    area_atuacao = models.CharField(max_length=100)

class Coordenador(Usuario):
    setor = models.CharField(max_length=100)

# ==============================================================================
# 3. ENTIDADES DE APOIO
# ==============================================================================

class EmpresaParceira(models.Model):
    razao_social = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    responsavel_legal = models.CharField(max_length=255)

    def __str__(self):
        return self.razao_social

class ModeloDocumento(models.Model):
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=30, choices=TipoDocumento.choices)
    versao = models.CharField(max_length=10)
    arquivo_modelo = models.FileField(upload_to='modelos/')

# ==============================================================================
# 4. PROCESSO DE ESTÁGIO E DOCUMENTAÇÃO
# ==============================================================================

class SolicitacaoEstagio(models.Model):
    data_abertura = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=StatusSolicitacao.choices, default=StatusSolicitacao.EM_PREENCHIMENTO)
    score_conformidade = models.FloatField(default=0.0)
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, related_name='solicitacoes')

class Documento(models.Model):
    nome_arquivo = models.CharField(max_length=255)
    tipo = models.CharField(max_length=30, choices=TipoDocumento.choices)
    data_envio = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=StatusDocumento.choices, default=StatusDocumento.ENVIADO)
    caminho_arquivo = models.FileField(upload_to='documentos_estagio/')
    solicitacao = models.ForeignKey(SolicitacaoEstagio, on_delete=models.CASCADE, related_name='documentos')
    modelo_referencia = models.ForeignKey(ModeloDocumento, on_delete=models.SET_NULL, null=True, blank=True)

class RelatorioEstagio(Documento):
    titulo = models.CharField(max_length=255)
    periodo_referencia = models.CharField(max_length=50)
    parecer = models.TextField(blank=True, null=True)
    conceito = models.CharField(max_length=50, blank=True, null=True)
    professor_avaliador = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True)

# ==============================================================================
# 5. PENDÊNCIAS, NOTIFICAÇÕES E VALIDAÇÕES
# ==============================================================================

class Pendencia(models.Model):
    tipo = models.CharField(max_length=50, choices=TipoPendencia.choices)
    descricao = models.TextField()
    obrigatoria = models.BooleanField(default=True)
    resolvida = models.BooleanField(default=False)
    solicitacao = models.ForeignKey(SolicitacaoEstagio, on_delete=models.CASCADE, related_name='pendencias')

class Notificacao(models.Model):
    tipo = models.CharField(max_length=50, choices=TipoNotificacao.choices)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)
    destinatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='notificacoes')
    solicitacao_origem = models.ForeignKey(SolicitacaoEstagio, on_delete=models.CASCADE, null=True, blank=True)

class ValidacaoAutomatica(models.Model):
    data_processamento = models.DateTimeField(auto_now_add=True)
    tempo_processamento_seg = models.IntegerField()
    regras_aplicadas = models.TextField()
    resultado = models.TextField()
    solicitacao = models.ForeignKey(SolicitacaoEstagio, on_delete=models.CASCADE)

class AnaliseExcecao(models.Model):
    motivo = models.TextField()
    decisao = models.CharField(max_length=30, choices=DecisaoCoordenacao.choices, null=True, blank=True)
    observacao = models.TextField(blank=True)
    data_analise = models.DateField(null=True, blank=True)
    solicitacao = models.OneToOneField(SolicitacaoEstagio, on_delete=models.CASCADE)
    coordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT)

class Assinatura(models.Model):
    data_assinatura = models.DateTimeField(auto_now_add=True)
    nome_assinante = models.CharField(max_length=255)
    cargo_assinante = models.CharField(max_length=100)
    hash_validacao = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE, related_name='assinaturas')
    empresa = models.ForeignKey(EmpresaParceira, on_delete=models.SET_NULL, null=True, blank=True)