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
```puml
@startuml


skinparam monochrome true
skinparam shadowing false



note right of R
Matrícula:
Digite sua matrícula ____________________

Tipo de Documento:
Selecione o tipo ________________________

Upload:
Escolher arquivo ________________________

Dados Complementares:
Descrição _______________________________
Data ___________________________________

----------------------------------------

[ Entrar / Enviar ]

----------------------------------------

Mensagem:
Arquivo inválido → envie PDF

Regras:
- Apenas PDF ou equivalentes
- Todos os documentos obrigatórios
end note

@enduml
```
###  Validação Automática

```puml
@startuml

skinparam monochrome true
skinparam shadowing false

rectangle "Validação de Documentos" {
Status:
Iniciando validação ____________________

Regras Legais:
Aplicando Lei 11.788/2008 _____________

Regras Institucionais:
Validando critérios internos ___________

Análise:
Identificando inconsistências __________

Score de Conformidade:
Calculando ____________________________

----------------------------------------

[ Processar ]
[ Atualizar ]

----------------------------------------

Mensagem:
Falha na leitura -> documento inválido

Resultado:
Validação registrada ___________________

Regras:
- Tempo máximo: 15 segundos
- Score baseado na conformidade
}

@enduml
```


### Identificar Pendências
```puml
@startuml


skinparam monochrome true
skinparam shadowing false



note right of R
Status:
Analisando resultados ___________________

Pendências:
Gerando lista ___________________________

Regras:
Associando erros às regras _____________

Retorno:
Enviando ao estudante ___________________

----------------------------------------

[ Processar ]
[ Atualizar ]

----------------------------------------

Mensagem:
Pendências identificadas

Detalhes:
Descrição clara da pendência ___________
Documento afetado ______________________

Regras de Negócio:
- Cada pendência deve ser clara
- Indicar documento afetado
end note

@enduml

```

###  Notificar Usuários
```puml
@startuml


skinparam monochrome true
skinparam shadowing false


note right
Atores:
Sistema, Estudante

Objetivo:
Informar eventos relevantes do processo

Pré-requisito:
Existência de solicitação ativa

----------------------------------------

Fluxo principal:
- O sistema identifica mudança de estado
- Gera notificação
- Envia ao estudante

----------------------------------------

Pós-requisito:
Usuário informado

----------------------------------------

Regras de negócio:
- Notificações em tempo real ou próximo disso
end note

@enduml




```

### Consultar Status da Solicitação
```puml
@startuml


skinparam monochrome true
skinparam shadowing false



note right of R
Ator:
Estudante

Objetivo:
Permitir acompanhamento do processo

Pré-requisito:
Solicitação existente

----------------------------------------

Fluxo principal:
- O estudante acessa suas solicitações
- O sistema exibe status:
  • Em validação
  • Pendente
  • Validado
  • Em exceção
- Exibe histórico do processo

----------------------------------------

Pós-requisito:
Status visualizado

----------------------------------------

Regras de negócio:
- Histórico deve ser imutável
end note

@enduml
```

###  Painel Gerencial
```puml
@startuml

skinparam monochrome true
skinparam shadowing false


note right of R
Ator:
Coordenação

Objetivo:
Monitorar o desempenho geral do sistema

Pré-requisito:
Coordenador autenticado

----------------------------------------

Fluxo principal:
- O coordenador acessa o painel
- O sistema exibe indicadores de desempenho
- O coordenador aplica filtros
- O sistema atualiza os indicadores conforme filtros aplicados

----------------------------------------

Pós-requisito:
Visão consolidada disponível

----------------------------------------

Regras de negócio:
- Dados devem ser atualizados em tempo real
end note

@enduml
```

###  Analisar Exceções
```puml
@startuml


skinparam monochrome true
skinparam shadowing false


note right of R
Ator:
Coordenação

Objetivo:
Tratar casos que não foram resolvidos automaticamente

Pré-requisito:
Solicitação marcada como exceção

----------------------------------------

Fluxo principal:
- O coordenador acessa o caso em exceção
- Analisa inconsistências identificadas
- Decide entre:
  • Aprovar
  • Solicitar ajuste
- O sistema registra a decisão tomada

----------------------------------------

Pós-requisito:
Caso resolvido manualmente

----------------------------------------

Regras de negócio:
- Intervenção manual só ocorre em exceções
end note

@enduml
```

### Avaliar Relatório de Estágio
```puml
@startuml


skinparam monochrome true
skinparam shadowing false


note right of R
Ator:
Professor

Objetivo:
Avaliar desempenho acadêmico do estudante

Pré-requisito:
Relatório disponível

----------------------------------------

Fluxo principal:
- O professor acessa o relatório do estudante
- Realiza leitura do conteúdo
- Emite parecer acadêmico
- Atribui conceito ao estudante
- O sistema registra a avaliação

----------------------------------------

Pós-requisito:
Avaliação registrada

----------------------------------------

Regras de negócio:
- Avaliação acadêmica é independente da validação legal
end note

@enduml
```
### Assinatura de Documentos
```puml
@startuml


skinparam monochrome true
skinparam shadowing false



note right of R
Ator:
Empresa Parceira

Objetivo:
Formalizar participação da empresa

Pré-requisito:
Documentos válidos

----------------------------------------

Fluxo principal:
- A empresa acessa o documento disponibilizado
- Verifica os dados apresentados
- Realiza assinatura digital
- O sistema registra a assinatura

----------------------------------------

Pós-requisito:
Documento assinado

----------------------------------------

Regras de negócio:
- Assinatura deve garantir autenticidade e integridade
end note

@enduml
```

### Acessar Modelos de Documentos
```puml
@startuml


skinparam monochrome true
skinparam shadowing false



note right of R
Ator:
Estudante

Objetivo:
Disponibilizar templates oficiais

Pré-requisito:
Usuário autenticado

----------------------------------------

Fluxo principal:
- O estudante acessa a área de modelos
- O sistema exibe lista de templates disponíveis
- O estudante visualiza os modelos disponíveis
- Realiza download do documento desejado

----------------------------------------

Pós-requisito:
Documento obtido

----------------------------------------

Regras de negócio:
- Modelos devem estar sempre atualizados conforme normas institucionais
end note

@enduml
```




## Conclusão

<p align = "justify">
A construção dos protótipos de baixa fidelidade permitiu visualizar de forma clara as funcionalidades e fluxos do sistema, facilitando a comunicação entre os envolvidos no projeto.
</p>


## Autor(es)

| Data     | Versão | Descrição                            | Autor(es)                                                                            |
| -------- | ------- | -------------------------------------- | ------------------------------------------------------------------------------------ |
| 15/04/26 | 1.0     | Criação do Prototipo               |   Gabriel Barreto, Guilherme Braz, Ísis Tavares, Mariana Faria e Matheus Alvarenga                                              |
