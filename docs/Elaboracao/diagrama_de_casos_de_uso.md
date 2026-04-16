---
id: diagrama_de_casos_de_uso
title: Diagrama de Casos de Uso
---
## Casos de uso
```plantuml
@startuml Sistema_Validacao_Estagios

left to right direction
skinparam actorStyle awesome

actor Estudante
actor "Empresa Parceira" as Empresa
actor Professor
actor Coordenacao
actor Sistema

' ===== CASOS PRINCIPAIS =====

usecase (UC01: Submeter Documentos de Estágio) as UC01
usecase (Selecionar Tipo de Documento) as UC01_1
usecase (Realizar Upload) as UC01_2
usecase (Preencher Dados Complementares) as UC01_3

usecase (UC02: Validação Automática) as UC02
usecase (Validar Regras Legais) as UC02_1
usecase (Validar Regras Institucionais) as UC02_2
usecase (Gerar Score de Conformidade) as UC02_3
usecase (Erro de Validação) as FA01

usecase (UC03: Identificar Pendências) as UC03
usecase (Gerar Lista de Inconsistências) as UC03_1
usecase (Retornar Correções ao Aluno) as UC03_2

usecase (UC04: Notificar Usuários) as UC04
usecase (Notificar Mudança de Status) as UC04_1
usecase (Notificar Pendências) as UC04_2

usecase (UC05: Consultar Status da Solicitação) as UC05
usecase (Visualizar Histórico) as UC05_1

usecase (UC06: Painel Gerencial) as UC06
usecase (Visualizar Indicadores) as UC06_1
usecase (Filtrar Solicitações) as UC06_2

usecase (UC07: Analisar Exceções) as UC07
usecase (Revisar Solicitação Inconsistente) as UC07_1
usecase (Aprovar Exceção) as UC07_2
usecase (Solicitar Ajuste Manual) as UC07_3

usecase (UC08: Avaliar Relatório de Estágio) as UC08
usecase (Ler Relatório) as UC08_1
usecase (Emitir Parecer) as UC08_2
usecase (Atribuir Conceito) as UC08_3

usecase (UC09: Assinatura de Documentos) as UC09
usecase (Validar Dados da Empresa) as UC09_1
usecase (Registrar Assinatura) as UC09_2

usecase (UC10: Acessar Modelos de Documentos) as UC10
usecase (Listar Modelos Disponíveis) as UC10_1
usecase (Realizar Download) as UC10_2

' ===== RELACIONAMENTOS ATORES =====

Estudante --> UC01
Estudante --> UC05
Estudante --> UC10

Empresa --> UC09

Professor --> UC08

Coordenacao --> UC06
Coordenacao --> UC07

Sistema --> UC02
Sistema --> UC03
Sistema --> UC04

' ===== INCLUDES =====

UC01 --> UC01_1 : <<include>>
UC01 --> UC01_2 : <<include>>
UC01 --> UC01_3 : <<include>>

UC02 --> UC02_1 : <<include>>
UC02 --> UC02_2 : <<include>>
UC02 --> UC02_3 : <<include>>

UC03 --> UC03_1 : <<include>>
UC03 --> UC03_2 : <<include>>

UC04 --> UC04_1 : <<include>>
UC04 --> UC04_2 : <<include>>

UC05 --> UC05_1 : <<include>>

UC06 --> UC06_1 : <<include>>
UC06 --> UC06_2 : <<include>>

UC07 --> UC07_1 : <<include>>
UC07 --> UC07_2 : <<extend>>
UC07 --> UC07_3 : <<extend>>

UC08 --> UC08_1 : <<include>>
UC08 --> UC08_2 : <<include>>
UC08 --> UC08_3 : <<include>>

UC09 --> UC09_1 : <<include>>
UC09 --> UC09_2 : <<include>>

UC10 --> UC10_1 : <<include>>
UC10 --> UC10_2 : <<include>>

' ===== EXTENSÕES (FALHAS) =====

FA01 .> UC02_1 : <<extend>>

' ===== NOTAS =====

note right of UC02
  Processo central do sistema:
  valida automaticamente com base na lei
  e regras institucionais, sem intervenção humana.
end note

note right of UC07
  Usado apenas quando o sistema
  não consegue decidir automaticamente.
end note

note right of UC08
  Avaliação acadêmica separada da validação legal.
end note

@enduml
```
---
# Explicação

## UC01 – Submeter Documentos de Estágio

Ator: Estudante
Objetivo: Permitir o envio estruturado dos documentos obrigatórios para validação.

Pré-requisito: Estudante autenticado e com solicitação ativa.

Fluxo principal:

O estudante acessa a área de submissão.
Seleciona o tipo de documento.
Realiza o upload.
Preenche dados complementares.
O sistema armazena os arquivos.

Fluxo alternativo:

Arquivo inválido → sistema rejeita e solicita novo envio.

Pós-requisito: Documentos registrados no sistema.

Regras de negócio:

Apenas formatos PDF ou equivalentes são aceitos.
Todos os documentos obrigatórios devem ser enviados.

---

## UC02 – Validação Automática

Ator: Sistema
Objetivo: Validar documentos com base em regras legais e institucionais.

Pré-requisito: Documentos submetidos.

Fluxo principal:

O sistema inicia a validação.
Aplica regras da Lei 11.788/2008.
Aplica regras institucionais.
Identifica inconsistências.
Calcula o score de conformidade.

Fluxo alternativo:

Falha na leitura → sistema marca como inválido.

Pós-requisito: Resultado de validação registrado.

Regras de negócio:

A validação deve ocorrer em até 15 segundos.
O score deve refletir o nível de conformidade dos documentos.

---

## UC03 – Identificar Pendências

Ator: Sistema
Objetivo: Detectar inconsistências e gerar correções automáticas.

Pré-requisito: Validação concluída.

Fluxo principal:

O sistema analisa os resultados.
Gera lista de pendências.
Associa cada erro a uma regra.
Retorna ao estudante.

Pós-requisito: Pendências registradas e exibidas.

Regras de negócio:

Cada pendência deve conter descrição clara.
Deve indicar exatamente o documento afetado.

---

## UC04 – Notificar Usuários

Atores: Sistema, Estudante
Objetivo: Informar eventos relevantes do processo.

Pré-requisito: Existência de solicitação ativa.

Fluxo principal:

O sistema identifica mudança de estado.
Gera notificação.
Envia ao estudante.

Pós-requisito: Usuário informado.

Regras de negócio:

Notificações devem ocorrer em tempo real ou próximo disso.

---

## UC05 – Consultar Status da Solicitação

Ator: Estudante
Objetivo: Permitir acompanhamento do processo.

Pré-requisito: Solicitação existente.

Fluxo principal:

O estudante acessa suas solicitações.
O sistema exibe status:
Em validação
Pendente
Validado
Em exceção
Exibe histórico.

Pós-requisito: Status visualizado.

Regras de negócio:

Histórico deve ser imutável.

---

## UC06 – Painel Gerencial

Ator: Coordenação
Objetivo: Monitorar o desempenho geral do sistema.

Pré-requisito: Coordenador autenticado.

Fluxo principal:

Acessa painel.
Visualiza indicadores.
Aplica filtros.

Pós-requisito: Visão consolidada disponível.

Regras de negócio:

Dados devem ser atualizados em tempo real.

---

## UC07 – Analisar Exceções

Ator: Coordenação
Objetivo: Tratar casos que não foram resolvidos automaticamente.

Pré-requisito: Solicitação marcada como exceção.

Fluxo principal:

Coordenador acessa caso.
Analisa inconsistências.
Decide:
Aprovar
Solicitar ajuste
Sistema registra decisão.

Pós-requisito: Caso resolvido manualmente.

Regras de negócio:

Intervenção manual só ocorre em exceções.

---

## UC08 – Avaliar Relatório de Estágio

Ator: Professor
Objetivo: Avaliar desempenho acadêmico do estudante.

Pré-requisito: Relatório disponível.

Fluxo principal:

Professor acessa relatório.
Realiza leitura.
Emite parecer.
Atribui conceito.

Pós-requisito: Avaliação registrada.

Regras de negócio:

Avaliação acadêmica é independente da validação legal.

---

## UC09 – Assinatura de Documentos

Ator: Empresa Parceira
Objetivo: Formalizar participação da empresa.

Pré-requisito: Documentos válidos.

Fluxo principal:

Empresa acessa documento.
Verifica dados.
Assina digitalmente.
Sistema registra.

Pós-requisito: Documento assinado.

Regras de negócio:

Assinatura deve garantir autenticidade e integridade.

---

## UC10 – Acessar Modelos de Documentos

Ator: Estudante
Objetivo: Disponibilizar templates oficiais.

Pré-requisito: Usuário autenticado.

Fluxo principal:

Acessa área de modelos.
Visualiza lista.
Realiza download.

Pós-requisito: Documento obtido.

Regras de negócio:

Modelos devem estar sempre atualizados conforme normas institucionais.

---

## Autor(es)
| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| 16/04/2026 | 1.0 | Criação do documento de casos de uso | Gabriel Barreto, Guilherme Braz, Ísis Tavares, Mariana Faria e Matheus Avarenga. |
