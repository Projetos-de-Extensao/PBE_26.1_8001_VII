---
id: prototipobaixa
title: Protótipo Baixa Fidelidade
---
## Introdução

<p align = "justify">
Um protótipo de baixa fidelidade é uma representação visual simplificada de um sistema ou aplicação, voltada para a comunicação universal de suas funcionalidades e fluxos. A proposta desse tipo de protótipo é oferecer uma forma clara e acessível de representar o funcionamento geral da aplicação.
</p>

## Metodologia

<p align = "justify">
O desenvolvimento dos protótipos de baixa fidelidade teve início com a coleta de ideias por meio de reuniões colaborativas e construção de mapas mentais, utilizando brainstorming para compreender as demandas dos usuários.
</p>

## Protótipo de baixa fidelidade



### Submeter Documentos de Estágio

```plantuml
@startsalt
{+
  **Submeter Documentos de Estágio**
  Matrícula:
  "Digite sua matrícula                  "
  Tipo de Documento:
  ^Selecione o tipo                      ^
  Upload:
  [ Escolher arquivo... ]
  Dados Complementares:
  Descrição: | "________________________"
  Data:      | "DD/MM/AAAA"
  --
  [   Entrar / Enviar   ]
  --
  **Mensagem:**
  <color:red>!! Arquivo inválido -> envie PDF</color>
  
  **Regras:**
  * Apenas PDF ou equivalentes
  * Todos os documentos obrigatórios
}
@endsalt
```

###  Validação Automática

```plantuml
@startsalt
{+
  **Validação de Documentos**
  Status:
  "Iniciando validação...               "
  
  Regras Legais:
  "Aplicando Lei 11.788/2008            "
  
  Regras Institucionais:
  "Validando critérios internos         "
  
  Análise:
  "Identificando inconsistências        "
  
  Score de Conformidade:
  "Calculando...                        "
  --
  [  Processar  ] | [  Atualizar  ]
  --
  **Mensagem:**
  <color:red>!! Falha na leitura -> documento inválido</color>
  
  **Resultado:**
  "Validação registrada                 "
  
  **Regras:**
  * Tempo máximo: 15 segundos
  * Score baseado na conformidade
}
@endsalt
```

### Identificar Pendências

```plantuml
@startsalt
{+
  **Identificar Pendências**
  Status:
  "Analisando resultados...               "
  
  Pendências:
  "Gerando lista...                       "
  
  Regras:
  "Associando erros às regras             "
  
  Retorno:
  "Enviando ao estudante...               "
  --
  [  Processar  ] | [  Atualizar  ]
  --
  **Mensagem:**
  <color:blue>i Pendências identificadas</color>
  
  **Detalhes:**
  Descrição: | "Descrição clara da pendência..."
  Documento: | "Documento afetado _____________"
  --
  **Regras de Negócio:**
  * Cada pendência deve ser clara
  * Indicar documento afetado
}
@endsalt
```

###  Notificar Usuários

```plantuml
@startsalt
{+
  **Caso de Uso: Notificar Usuários**
  --
  **Atores:** | Sistema, Estudante
  **Objetivo:** | Informar eventos relevantes do processo
  **Pré-requisito:**| Existência de solicitação ativa
  --
  **Fluxo Principal:**
  1. O sistema identifica mudança de estado
  2. Gera notificação
  3. Envia ao estudante
  --
  **Pós-requisito:**| Usuário informado
  --
  **Regras de Negócio:**
  * Notificações em tempo real ou próximo disso
}
@endsalt
```

### Consultar Status da Solicitação

```plantuml
@startsalt
{+
  **Consulta: Status da Solicitação**
  --
  **Ator:** | Estudante
  **Objetivo:** | Permitir acompanhamento do processo
  **Pré-requisito:** | Solicitação existente
  --
  **Fluxo Principal:**
  1. O estudante acessa suas solicitações
  2. O sistema exibe o status atual:
  ^ Status: Em validação | Pendente | Validado | Em exceção ^
  
  **Histórico do Processo (Imutável):**
  {#
    Data       | Evento               | Status
    10/04/2026 | Upload de Documentos | Recebido
    11/04/2026 | Validação Automática | Em processamento
    12/04/2026 | Análise de Regras    | Pendente
  }
  --
  **Pós-requisito:** | Status visualizado
  --
  **Regras de Negócio:**
  * Histórico deve ser imutável
}
@endsalt
```

###  Painel Gerencial

```plantuml
@startsalt
{+
  **Painel Gerencial (Coordenação)**
  --
  **Ator:** | Coordenação
  **Objetivo:** | Monitorar o desempenho geral do sistema
  **Pré-requisito:** | Coordenador autenticado
  --
  **Interface de Monitoramento:**
  {
    Filtros: | ^Período: Últimos 30 dias^ | ^Status: Todos^ | [ Aplicar Filtros ]
  }
  ---
  **Indicadores de Desempenho:**
  {
    Taxa de Aprovação: | [==== 88% ====]
    Tempo Médio:       | "12.5 segundos"
    Solicitações:      | "1.240 processadas"
  }
  --
  **Fluxo Principal:**
  1. O coordenador acessa o painel
  2. O sistema exibe indicadores de desempenho
  3. O coordenador aplica filtros
  4. O sistema atualiza os indicadores em tempo real
  --
  **Pós-requisito:** | Visão consolidada disponível
  --
  **Regras de Negócio:**
  * Dados devem ser atualizados em tempo real
}
@endsalt
```

###  Analisar Exceções

```plantuml
@startsalt
{+
  **Tratamento de Exceções (Coordenação)**
  --
  **Ator:** | Coordenação
  **Objetivo:** | Tratar casos não resolvidos automaticamente
  **Pré-requisito:** | Solicitação marcada como exceção
  --
  **Análise de Caso:**
  "ID Solicitação: #88293"
  "Inconsistência: Assinatura não reconhecida pelo OCR"
  --
  **Decisão Manual:**
  {
    (X) Aprovar Documento
    ( ) Solicitar Ajuste / Novo Upload
  }
  [ Registrar Decisão ]
  --
  **Fluxo Principal:**
  1. O coordenador acessa o caso em exceção
  2. Analisa inconsistências identificadas
  3. Decide entre Aprovar ou Solicitar ajuste
  4. O sistema registra a decisão tomada
  --
  **Pós-requisito:** | Caso resolvido manualmente
  --
  **Regras de Negócio:**
  * Intervenção manual só ocorre em exceções
}
@endsalt
```

### Avaliar Relatório de Estágio

```plantuml
@startsalt
{+
  **Avaliação de Relatório Acadêmico**
  --
  **Ator:** | Professor
  **Objetivo:** | Avaliar desempenho acadêmico do estudante
  **Pré-requisito:** | Relatório disponível
  --
  **Área de Avaliação:**
  Relatório: | [ Abrir Relatório_Estagio.pdf ]
  Parecer Acadêmico:
  "Digite aqui as observações sobre o desempenho...  "
  "                                                  "
  
  Conceito/Nota:
  ^ Selecionar Conceito (A, B, C...) ^
  --
  [  Registrar Avaliação  ]
  --
  **Fluxo Principal:**
  1. O professor acessa o relatório do estudante
  2. Realiza leitura do conteúdo
  3. Emite parecer acadêmico
  4. Atribui conceito ao estudante
  5. O sistema registra a avaliação
  --
  **Pós-requisito:** | Avaliação registrada
  --
  **Regras de Negócio:**
  * Avaliação acadêmica é independente da validação legal
}
@endsalt
```

### Assinatura de Documentos

```plantuml
@startsalt
{+
  **Portal de Assinatura Digital (Empresa Parceira)**
  --
  **Ator:** | Empresa Parceira
  **Objetivo:** | Formalizar participação da empresa
  **Pré-requisito:** | Documentos válidos
  --
  **Documento para Conferência:**
  [ Visualizar Termo_de_Compromisso.pdf ]
  
  **Autenticação da Assinatura:**
  {
    Método: | ^Certificado Digital (e-CNPJ) | Token SMS | Assinatura Gov.br^
    Status: | "Aguardando confirmação..."
  }
  [ Realizar Assinatura Digital ]
  --
  **Fluxo Principal:**
  1. A empresa acessa o documento disponibilizado
  2. Verifica os dados apresentados
  3. Realiza assinatura digital
  4. O sistema registra a assinatura
  --
  **Pós-requisito:** | Documento assinado
  --
  **Regras de Negócio:**
  * Assinatura deve garantir autenticidade e integridade
}
@endsalt
```

### Acessar Modelos de Documentos

```plantuml
@startsalt
{+
  **Área de Downloads: Modelos de Documentos**
  --
  **Ator:** | Estudante
  **Objetivo:** | Disponibilizar templates oficiais
  **Pré-requisito:** | Usuário autenticado
  --
  **Templates Disponíveis:**
  {#
    Nome do Documento             | Versão | Ação
    Termo de Compromisso (TCE)    | v2.1   | [ Download ]
    Plano de Atividades           | v1.0   | [ Download ]
    Relatório de Atividades       | v3.4   | [ Download ]
    Rescisão de Contrato          | v2.0   | [ Download ]
  }
  --
  **Fluxo Principal:**
  1. O estudante acessa a área de modelos
  2. O sistema exibe lista de templates disponíveis
  3. O estudante visualiza os modelos disponíveis
  4. Realiza download do documento desejado
  --
  **Pós-requisito:** | Documento obtido
  --
  **Regras de Negócio:**
  * Modelos atualizados conforme normas institucionais
}
@endsalt
```




## Conclusão

<p align = "justify">
A construção dos protótipos de baixa fidelidade permitiu visualizar de forma clara as funcionalidades e fluxos do sistema, facilitando a comunicação entre os envolvidos no projeto.
</p>


## Autor(es)

| Data     | Versão | Descrição                            | Autor(es)                                                                            |
| -------- | ------- | -------------------------------------- | ------------------------------------------------------------------------------------ |
| 16/04/26 | 1.0     | Criação do Prototipo               |   Gabriel Barreto, Guilherme Braz, Ísis Tavares, Mariana Faria e Matheus Alvarenga                                              |
