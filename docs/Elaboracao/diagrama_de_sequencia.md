---
id: diagrama_de_sequencia
title: Diagrama de Sequência
---

## Diagrama de Sequência

### Fluxo: Publicar Postagem

```plantuml
@startuml PublicarPostagem

actor Usuario
participant "Frontend" as FE
participant "API REST" as API
participant "PostagemViewSet" as PV
database "Banco de Dados" as DB

Usuario -> FE: Preenche conteúdo e envia
FE -> API: POST /api/postagens/\n{ conteudo, visibilidade }
API -> PV: perform_create(serializer)
PV -> DB: INSERT Postagem
DB --> PV: Postagem criada
PV --> API: HTTP 201 Created
API --> FE: { id, conteudo, dataPublicacao, visibilidade }
FE --> Usuario: Postagem exibida no feed

@enduml
```

### Fluxo: Enviar Mensagem

```plantuml
@startuml EnviarMensagem

actor Remetente
participant "Frontend" as FE
participant "API REST" as API
participant "MensagemViewSet" as MV
database "Banco de Dados" as DB

Remetente -> FE: Escreve mensagem e envia
FE -> API: POST /api/mensagens/\n{ conteudo, destinatario }
API -> MV: perform_create(serializer)
MV -> DB: INSERT Mensagem
DB --> MV: Mensagem criada
MV --> API: HTTP 201 Created
API --> FE: { id, conteudo, dataEnvio, lida: false }
FE --> Remetente: Mensagem enviada

@enduml
```

### Fluxo: Interagir com Postagem

```plantuml
@startuml InteragirPostagem

actor Usuario
participant "Frontend" as FE
participant "API REST" as API
participant "InteracaoViewSet" as IV
database "Banco de Dados" as DB

Usuario -> FE: Clica em curtir / comentar
FE -> API: POST /api/interacoes/\n{ tipo, postagem, conteudo }
API -> IV: perform_create(serializer)
IV -> DB: INSERT Interacao
DB --> IV: Interacao criada
IV --> API: HTTP 201 Created
API --> FE: { id, tipo, data }
FE --> Usuario: Reação registrada

@enduml
```

## Versionamento

| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| 28/05/2026 | 1.0 | Criação do diagrama de sequência | Gabriel Barreto, Guilherme Braz, Ísis Tavares, Mariana Faria e Matheus Alvarenga |
