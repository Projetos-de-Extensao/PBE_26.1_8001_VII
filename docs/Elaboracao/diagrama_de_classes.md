---
id: diagrama_de_classes
title: Diagrama de Classes
---

## Diagrama de Classes

```plantuml
@startuml Diagrama_Classes_Sistema_Validacao_Estagios

skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam ArrowColor #333333
skinparam ClassBorderColor #555555

enum StatusSolicitacao {
  EM_PREENCHIMENTO
  SUBMETIDA
  EM_VALIDACAO
  COM_PENDENCIAS
  EM_ANALISE_EXCECAO
  APROVADA
  REPROVADA
}

enum TipoDocumento {
  CONTRATO
  TERMO_COMPROMISSO
  RELATORIO_PARCIAL
  RELATORIO_FINAL
  APOLICE_SEGURO
  OUTRO
}

enum StatusDocumento {
  ENVIADO
  VALIDADO
  COM_PENDENCIA
  REJEITADO
  ASSINADO
}

enum TipoNotificacao {
  STATUS_ALTERADO
  PENDENCIA_IDENTIFICADA
  PRAZO_PROXIMO
  DOCUMENTO_ASSINADO
}

enum TipoPendencia {
  DADO_AUSENTE
  ASSINATURA_FALTANTE
  DOCUMENTO_INVALIDO
  INCONSISTENCIA_LEGAL
  INCONSISTENCIA_INSTITUCIONAL
}

enum DecisaoCoordenacao {
  APROVAR_EXCECAO
  SOLICITAR_AJUSTE
  REPROVAR
}

class Usuario {
  - id: Long
  - nome: String
  - emailInstitucional: String
  - senha: String
  - ativo: Boolean
  + autenticar(): Boolean
  + logout(): void
  + atualizarDados(): void
}

class Estudante {
  - matricula: String
  - curso: String
  - periodo: int
  + abrirSolicitacao(): void
  + submeterDocumento(): void
  + consultarStatus(): void
  + visualizarPendencias(): void
}

class Professor {
  - areaAtuacao: String
  + avaliarRelatorio(): void
  + emitirParecer(): void
  + atribuirConceito(): void
}

class Coordenador {
  - setor: String
  + visualizarPainel(): void
  + analisarExcecao(): void
  + registrarDecisao(): void
}

class EmpresaParceira {
  - idEmpresa: Long
  - razaoSocial: String
  - cnpj: String
  - responsavelLegal: String
  + confirmarDados(): void
  + assinarDocumento(): void
}

class SolicitacaoEstagio {
  - id: Long
  - dataAbertura: Date
  - status: StatusSolicitacao
  - scoreConformidade: double
  + registrarSubmissao(): void
  + atualizarStatus(): void
  + calcularScore(): double
  + listarPendencias(): List<Pendencia>
}

class Documento {
  - id: Long
  - nomeArquivo: String
  - tipo: TipoDocumento
  - dataEnvio: Date
  - status: StatusDocumento
  - caminhoArquivo: String
  + validarFormato(): Boolean
  + armazenar(): void
  + atualizarStatus(): void
}

class ValidacaoAutomatica {
  - id: Long
  - dataProcessamento: Date
  - tempoProcessamentoSeg: int
  - regrasAplicadas: String
  - resultado: String
  + validarLeiEstagio(): void
  + validarRegrasInstitucionais(): void
  + gerarScore(): double
  + detectarPendencias(): List<Pendencia>
}

class Pendencia {
  - id: Long
  - tipo: TipoPendencia
  - descricao: String
  - obrigatoria: Boolean
  - resolvida: Boolean
  + gerarDescricao(): void
  + marcarResolvida(): void
}

class Notificacao {
  - id: Long
  - tipo: TipoNotificacao
  - mensagem: String
  - dataEnvio: Date
  - lida: Boolean
  + enviar(): void
  + marcarComoLida(): void
}

class ModeloDocumento {
  - id: Long
  - nome: String
  - tipo: TipoDocumento
  - versao: String
  - arquivoModelo: String
  + disponibilizarDownload(): void
  + atualizarVersao(): void
}

class Assinatura {
  - id: Long
  - dataAssinatura: Date
  - nomeAssinante: String
  - cargoAssinante: String
  - hashValidacao: String
  + registrar(): void
  + validarIntegridade(): Boolean
}

class RelatorioEstagio {
  - id: Long
  - titulo: String
  - periodoReferencia: String
  - parecer: String
  - conceito: String
  + registrarParecer(): void
  + atribuirConceito(): void
}

class AnaliseExcecao {
  - id: Long
  - motivo: String
  - decisao: DecisaoCoordenacao
  - observacao: String
  - dataAnalise: Date
  + registrarAnalise(): void
  + aprovarExcecao(): void
  + solicitarAjuste(): void
  + reprovar(): void
}

Usuario <|-- Estudante
Usuario <|-- Professor
Usuario <|-- Coordenador

Estudante "1" --> "0..*" SolicitacaoEstagio : realiza >
SolicitacaoEstagio "1" *-- "1..*" Documento : contém >
SolicitacaoEstagio "1" *-- "0..*" Pendencia : gera >
SolicitacaoEstagio "1" --> "0..*" Notificacao : dispara >
SolicitacaoEstagio "1" --> "0..1" AnaliseExcecao : pode gerar >
SolicitacaoEstagio "1" --> "0..1" RelatorioEstagio : inclui >

ValidacaoAutomatica "1" --> "1" SolicitacaoEstagio : processa >
ValidacaoAutomatica "1" --> "1..*" Documento : analisa >

Professor "1" --> "0..*" RelatorioEstagio : avalia >
Coordenador "1" --> "0..*" AnaliseExcecao : decide >
EmpresaParceira "1" --> "0..*" Assinatura : realiza >

Documento "1" --> "0..*" Assinatura : pode conter >
Documento "0..*" --> "1" ModeloDocumento : segue >
RelatorioEstagio --|> Documento

Notificacao "0..*" --> "1" Usuario : destinatário >

@enduml
```

## Descrição das Classes

## Usuario: Classe base responsável por representar os usuários do sistema. Armazena dados comuns de autenticação e identificação, como nome, e-mail institucional, senha e status de ativação.

## Estudante: Representa o aluno que solicita a validação do estágio. Pode abrir solicitações, enviar documentos, consultar status e visualizar pendências.

## Professor: Representa o docente responsável pela análise acadêmica dos relatórios de estágio. Pode avaliar relatórios, emitir pareceres e atribuir conceitos.

## Coordenador: Representa o responsável pelo acompanhamento gerencial do processo. Pode visualizar indicadores, analisar exceções e registrar decisões em casos não resolvidos automaticamente.

## EmpresaParceira: Representa a organização que oferece a oportunidade de estágio. É responsável por confirmar dados institucionais e realizar assinaturas nos documentos exigidos.

## SolicitacaoEstagio: Classe central do sistema. Representa cada processo de validação de estágio iniciado por um estudante, armazenando data de abertura, status atual, score de conformidade e vínculos com documentos, pendências e análises.

## Documento: Representa os arquivos submetidos no sistema, como contrato, termo de compromisso, apólice e relatórios. Armazena informações sobre tipo, nome do arquivo, data de envio, caminho de armazenamento e status do documento.

## ValidacaoAutomatica: Representa o módulo responsável por aplicar as regras legais e institucionais aos documentos submetidos. Executa a validação, detecta inconsistências, calcula o score de conformidade e gera pendências.

## Pendencia: Representa problemas identificados durante a validação automática, como ausência de dados, assinaturas faltantes ou inconsistências legais e institucionais. Cada pendência possui descrição e estado de resolução.

## Notificacao: Representa os avisos enviados pelo sistema aos usuários sobre alterações de status, pendências identificadas, prazos próximos ou documentos assinados.

## ModeloDocumento: Representa os modelos padronizados de documentos disponibilizados pela instituição para download, como formulários e termos oficiais.

## Assinatura: Representa o registro da assinatura realizada em um documento, armazenando dados como nome do assinante, cargo, data da assinatura e mecanismo de validação.

## RelatorioEstagio: Representa um tipo específico de documento ligado à avaliação acadêmica. Além das informações básicas de documento, permite registrar parecer e conceito atribuídos pelo professor.

## AnaliseExcecao: Representa o tratamento manual feito pela coordenação quando uma solicitação não pode ser resolvida de forma totalmente automática. Armazena o motivo, a decisão tomada, observações e data da análise.



## Versionamento

## Versão 1.0: Definição inicial das classes principais do sistema, contemplando usuários, solicitações, documentos, validação automática, pendências e notificações.

## Versão 1.1: Inclusão das classes RelatorioEstagio e AnaliseExcecao para separar a avaliação acadêmica da validação documental e representar a atuação da coordenação em casos excepcionais.

## Versão 1.2: Refinamento dos relacionamentos entre as classes e inclusão de enums de apoio para padronizar status, tipos de documentos, notificações, pendências e decisões.

## Versão atual: Estrutura orientada a objetos compatível com a proposta do sistema de validação de estágios, com foco em automação, rastreabilidade, apoio à coordenação e conformidade com regras institucionais e legais.

| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| 16/04/2026 | 1.0 | Criação do diagrama de classes | Gabriel Barreto, Guilherme Braz, Ísis Tavares, Mariana Faria e Matheus Alvarenga |
