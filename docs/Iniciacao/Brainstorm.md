# Brainstorm

## Introdução

O brainstorm é uma técnica de elicitação de requisitos que consiste em reunir a equipe e discutir sobre diversos tópicos gerais do projeto apresentados no documento problema de negócio. No brainstorm o diálogo é incentivado e críticas são evitadas para permitir que todos colaborem com suas próprias ideias.

## Metodologia

A equipe se reuniu para debater ideias gerais sobre o projeto via Discord, começou às 19:00 e terminou às 22:00, onde o Guilherme Braz foi o moderador, direcionando a equipe com questões pré-elaboradas, e transcrevendo as respostas para o documento.

---

## Perguntas e Respostas (Versão 1.0)

### 1. Qual o objetivo principal da aplicação?

1. Deve ser uma plataforma capaz de submeter, acompanhar e validar documentos de estágio de forma automatizada.
2. A plataforma deve fornecer um sistema de análise que verifique a conformidade dos contratos com a legislação vigente e as diretrizes acadêmicas.
3. O objetivo da aplicação é automatizar o processo de validação de estágios, reduzindo tempo e erros manuais.
4. O principal objetivo da aplicação é a otimização do fluxo administrativo e a padronização da verificação dos contratos de estágio.
5. A plataforma deve gerenciar o recebimento, processamento e retorno das validações dos estágios, incluindo relatórios detalhados para alunos e coordenação.

---

### 2. Como será o processo para cadastrar um novo cliente?

1. O moderador deverá fazer login e acessar a área de gerenciamento de usuários para autorizar novos cadastros.
2. O cliente deverá preencher um formulário com seus dados pessoais e acadêmicos.
3. Com o usuário logado, ele deverá validar as informações inseridas e confirmar o cadastro no sistema.
4. O cliente fará uso de um token para autenticar as requisições.
5. O cliente poderá enviar os dados e o sistema irá verificar sua legibilidade.

---

### 3. Como será a forma de adicionar produtos (estágios)?

1. O cliente, ao cadastrar um estágio, deverá inserir as informações do contrato e anexar os documentos necessários.
2. O "produto" (estágio) possui dados como carga horária, empresa concedente, período e informações do aluno.
3. O estágio será enviado para processamento, onde passará pelas validações automáticas definidas no sistema.
4. O estágio poderá ser aprovado ou reprovado, com retorno detalhado indicando possíveis pendências ou inconsistências.

---

### 4. Outras perguntas pertinentes ao contexto

1. Com a centralização das informações na plataforma, será possível acompanhar o status das validações em tempo real?
2. O cliente poderá consultar o histórico de envios e verificar os resultados das análises realizadas?
3. O cliente poderá receber feedback detalhado sobre pendências e realizar ajustes para nova submissão dos documentos?

---

### 5. Como o cliente adicionará os documentos?

1. O cliente deverá acessar a plataforma e preencher um formulário com os dados do estágio, anexando os documentos necessários para submissão.

---

### 6. Quais informações seriam interessantes para o cliente?

1. **Status da validação:** aprovado, reprovado ou pendente, com detalhes das inconsistências.
2. **Histórico:** acesso a submissões anteriores, documentos enviados e feedbacks recebidos.
3. **Regras e Prazos:** visualização das normas acadêmicas/legais e orientações para aprovação.

---

### Requisitos Elicitados

| ID | Descrição |
| :--- | :--- |
| **BS01** | O cliente poderá realizar cadastro na plataforma informando dados pessoais e acadêmicos. |
| **BS02** | O cliente poderá autenticar-se no sistema utilizando credenciais seguras. |
| **BS03** | O cliente poderá submeter documentos de estágio para validação. |
| **BS04** | O cliente poderá acompanhar o status da validação em tempo real. |
| **BS05** | O cliente poderá visualizar o histórico de submissões realizadas. |
| **BS06** | O cliente poderá receber feedback detalhado sobre pendências ou reprovações. |
| **BS07** | O cliente poderá atualizar seus dados cadastrais. |
| **BS08** | O cliente poderá reenviar documentos após correções. |
| **BS09** | O cliente poderá consultar regras e orientações para validação de estágio. |
| **BS10** | O produto deverá processar os dados dos contratos submetidos. |
| **BS11** | O produto deverá aplicar regras de validação baseadas na Lei 11.788/08 e diretrizes institucionais. |
| **BS12** | O produto deverá retornar o resultado da validação (aprovado ou reprovado). |
| **BS13** | O produto deverá gerar relatórios detalhados com justificativas das análises. |
| **BS14** | O produto deverá armazenar os dados e histórico das validações em banco de dados. |
| **BS15** | O produto deverá garantir a integridade e segurança das informações processadas. |

---

## Conclusão

Através da aplicação da técnica, foi possível elicitar os requisitos fundamentais para o desenvolvimento do sistema de validação de estágios.

## Referências Bibliográficas

> BARBOSA, S. D. J; DA SILVA, B. S. **Interação humano-computador**. Elsevier