---
id: diagrama_de_classes
title: Diagrama de Classes
---

## Diagrama de Classes

```plantuml
@startuml DiagramaDeClasses

skinparam classAttributeIconSize 0
skinparam classFontStyle bold
skinparam ArrowColor #333333
skinparam ClassBorderColor #555555

enum TipoInteracao {
  CURTIDA
  COMENTARIO
  COMPARTILHAMENTO
}

class Conta {
  - id: Long
  - email: String
  - senha: String
  - dataCriacao: DateTime
  - ativo: Boolean
  - token: String
  + criar(): void
  + entrar(): void
  + alterar(): void
  + recuperarSenha(): void
  + excluirLogico(): void
  + visualizar(): Conta
}

class Perfil {
  - id: Long
  - nome: String
  - foto: String
  - bio: String
  - dataNascimento: Date
  + editar(): void
  + pesquisar(): List~Perfil~
  + visualizar(): Perfil
  + seguir(perfil: Perfil): void
  + deixarDeSeguir(perfil: Perfil): void
}

class Postagem {
  - id: Long
  - conteudo: String
  - dataPublicacao: DateTime
  - visibilidade: Boolean
  + criar(): void
  + excluir(): void
  + visualizar(): Postagem
}

class Interacao {
  - id: Long
  - tipo: TipoInteracao
  - conteudo: String
  - data: DateTime
  + interagir(): void
}

class Mensagem {
  - id: Long
  - conteudo: String
  - dataEnvio: DateTime
  - lida: Boolean
  + criar(): void
  + excluir(): void
  + visualizar(): Mensagem
}

' Relacionamentos
Conta "1" -- "1" Perfil : possui >

Perfil "1" --> "0..*" Postagem : publica >
Perfil "1" --> "0..*" Mensagem : envia >
Perfil "0..*" --> "0..*" Perfil : segue >

Postagem "1" --> "0..*" Interacao : recebe >

Mensagem "1" --> "1" Perfil : destinatário >

@enduml
```

## Descrição das Classes

### Conta
Representa as credenciais de acesso do usuário. Gerencia autenticação, recuperação de senha e exclusão lógica (soft delete).

### Perfil
Dados públicos do usuário. Um perfil pode seguir outros perfis, publicar postagens e enviar mensagens.

### Postagem
Conteúdo público criado pelo usuário. Pode receber interações (curtidas, comentários e compartilhamentos).

### Interacao
Representa as reações a uma postagem: curtida, comentário ou compartilhamento.

### Mensagem
Comunicação privada entre dois perfis.

## Versionamento

| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| 16/04/2026 | 1.0 | Criação do diagrama de classes | Gabriel Barreto, Guilherme Braz, Ísis Tavares, Mariana Faria e Matheus Alvarenga |
