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
Iniciamos o projeto através dos levantamentos iniciais da equipe, após discussões a ferramenta Figma foi selecionada para produzir o protótipo de alta fidelidade com auxílio do Material Design Color Tool.
</p>

## Protótipo de alta fidelidade

### Versão 1.0

### Tela Login
```puml
@startuml
title UC01 – Submeter Documentos de Estágio

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
### Tela Cadastro 1

```puml
@startuml
title UC02 – Validar Documentos

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


### Tela Cadastro 2
```puml
@startuml
title UC03 – Detectar Inconsistências

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

### Tela Esqueceu Senha
### Tela do Feed
```puml
@startuml
title UC04 – Notificações do Processo

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

### Tela Feed com configurações
```puml
@startuml
title UC05 – Acompanhamento do Processo

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

### Tela Perfil
```puml
@startuml
title UC06 – Painel Gerencial

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

### Tela Cadastrar torneio 1
```puml
@startuml
title UC07 – Analisar Exceções

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

### Tela Cadastrar torneio 2
```puml
@startuml
title UC08 – Avaliar Relatório de Estágio

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
### Tela Cadastrar torneio 3
```puml
@startuml
title UC09 – Assinatura de Documentos

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

### Tela Cadastrar torneio 4
```puml
@startuml
title UC10 – Acessar Modelos de Documentos

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
### Tela com meus torneios

[![Prototipo 12](../assets/Prototipo/image.png)](../assets/Prototipo/image.png)

### Tela de inscrição em torneio

[![Prototipo 13](../assets/Prototipo/image.png)](../assets/Prototipo/image.png)

<p align = "justify">
Na primeira versão do protótipo utilizamos a ferramenta <a href="https://material.io/resources/color/#!/?view.left=0&view.right=0">Material Design Color Tool</a>  para auxiliar na criação da paleta de cores do aplicativo, definimos as cores base do aplicativo mas as cores definidas para as telas 12 e 13 ainda não foram decididas.
</p>

### Versão 2.0

### Versão 1.0

### Tela Login

[![Prototipo 1](../assets/Prototipo/image.png)](../assets/Prototipo/image.png)

### Tela Cadastro 1

[![Prototipo 2](../assets/Prototipo/image.png)](../assets/Prototipo/image.png)

### Tela Cadastro 2

[![Prototipo 3](../assets/Prototipo/image.png)](../assets/Prototipo/image.png)

### Tela Esqueceu Senha

[![Prototipo 4](../assets/Prototipo/image.png)](../assets/Prototipo/image.png)

### Tela do Feed

[![Prototipo 5](../assets/Prototipo/image.png)](../assets/Prototipo/image.png)

### Tela Feed com configurações

[![Prototipo 6](../assets/Prototipo/image.png)](../assets/Prototipo/image.png)

### Tela Perfil

[![Prototipo 7](../assets/Prototipo/image.png)](../assets/Prototipo/image.png)

### Tela Cadastrar torneio 1

[![Prototipo 8](../assets/Prototipo/image.png)](../assets/Prototipo/image.png)

### Tela Cadastrar torneio 2

[![Prototipo 9](../assets/Prototipo/image.png)](../assets/Prototipo/image.png)

### Tela Cadastrar torneio 3

[![Prototipo 10](../assets/Prototipo/image.png)](../assets/Prototipo/image.png)

### Tela Cadastrar torneio 4

[![Prototipo 11](../assets/Prototipo/image.png)](../assets/Prototipo/image.png)

### Tela com meus torneios

[![Prototipo 12](../assets/Prototipo/image.png)](../assets/Prototipo/image.png)

### Tela de inscrição em torneio

[![Prototipo 13](../assets/Prototipo/image.png)](../assets/Prototipo/image.png)

link para o `<a href="https://www.figma.com/">`Protótipo`</a>`

## Conclusão

<p align = "justify">
A partir da elaboração do protótipo foi possível ter uma noção inicial da interface do usuário, definindo fluxo, paleta de cores, botões, app bars e diversas outras funcionalidades
</p>

## Referências

> Material Design Color Tool. Disponível em:  https://material.io/resources/color/#!/?view.left=0&view.right=0

> PMI. Um guia do conhecimento em gerenciamento de projetos. Guia PMBOK® 5a. ed. EUA: Project Management Institute, 2013.

> Ferramenta Figma. Disponível em https://www.figma.com

## Autor(es)

| Data     | Versão | Descrição                            | Autor(es)                                                                            |
| -------- | ------- | -------------------------------------- | ------------------------------------------------------------------------------------ |
| 07/09/20 | 1.0     | Criação do documento                 | Lucas Alexandre e Matheus Estanislau                                                 |
| 07/09/20 | 1.1     | Adicionado as imagens do protótipo    | Lucas Alexandre e Matheus Estanislau                                                 |
| 07/09/20 | 1.2     | Adicionado conclusão e referências   | Lucas Alexandre e Matheus Estanislau                                                 |
| 26/10/20 | 2.0     | Adicionada a versão 2.0 do protótipo | João Pedro, Lucas Alexandre, Matheus Estanislau, Moacir Mascarenha e Renan Cristyan |
