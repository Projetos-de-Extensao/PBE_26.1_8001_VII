---
id: dt
title: Design Thinking
---

## Design Thinking

### 1. Capa

- **Título do Projeto:** Plataforma de Validação de Estágio — IBMEC
- **Nome da Equipe:** Gabriel Barreto, Guilherme Braz, Ísis Tavares, Mariana Faria e Matheus Alvarenga
- **Data:** 16/04/2026
- **Organização:** IBMEC

---

### 2. Introdução

#### Contexto do Projeto

A gestão de estágios no IBMEC envolve um processo burocrático extenso: o aluno precisa submeter documentos como o Termo de Compromisso de Estágio (TCE), plano de atividades e relatórios periódicos, que são verificados manualmente pela coordenação e professores orientadores. Esse processo é lento, sujeito a erros e pouco padronizado, gerando atrasos na aprovação e dificuldades tanto para os alunos quanto para a administração.

#### Objetivo

Desenvolver uma plataforma backend que automatize a validação dos documentos de estágio, verificando a conformidade com a Lei nº 11.788/2008 e com as normas acadêmicas do IBMEC, reduzindo o tempo de análise e os erros humanos.

#### Público-Alvo

- Alunos do IBMEC em processo de estágio
- Coordenação acadêmica e professores orientadores
- Pró-Reitoria Acadêmica
- Empresas concedentes de estágio

#### Escopo

O projeto abrange o desenvolvimento de um serviço backend com rotas de API para recebimento, processamento e retorno das validações dos documentos de estágio, com base em regras de negócio definidas pela legislação e pela instituição.

---

### 3. Fases do Design Thinking

#### 3.1. Empatia

**Pesquisa:**

Para entender o problema, a equipe realizou pesquisa sobre:

- A Lei nº 11.788/2008 (Lei do Estágio), que define obrigações de todas as partes envolvidas
- As Diretrizes Curriculares Nacionais do MEC, que regulamentam o estágio por tipo de curso
- O regulamento interno do IBMEC, que define prazos, documentos exigidos e fluxos de aprovação
- Sistemas existentes como o SIA (IBMEC), SIGAA e plataformas de intermediação como CIEE e Nube

**Insights:**

- A validação manual dos documentos é demorada e inconsistente entre diferentes orientadores
- Os alunos frequentemente têm dúvidas sobre quais documentos enviar e quais regras seguem para aprovação
- A falta de feedback imediato faz com que os alunos reenviem documentos incorretos várias vezes
- A coordenação gasta tempo excessivo em tarefas repetitivas de verificação de conformidade
- A maioria dos sistemas existentes foca apenas no controle burocrático, sem automação inteligente

**Personas:**

**Persona 1 — Aluno Estagiário**
> Lucas, 21 anos, cursando Engenharia de Computação no IBMEC. Está iniciando seu primeiro estágio não obrigatório e tem dúvidas sobre quais documentos precisa enviar, quais são os prazos e como saber se seu estágio foi aprovado. Fica ansioso quando não recebe retorno da coordenação.

**Persona 2 — Coordenador Acadêmico**
> Carla, 38 anos, coordenadora do curso de Administração. Recebe dezenas de solicitações de estágio por semestre e precisa verificar manualmente cada documento. Frequentemente encontra erros simples como carga horária incorreta ou documentos faltantes, o que gera retrabalho para ela e para o aluno.

---

#### 3.2. Definição

**Problema Central:**

> *"Como podemos automatizar a validação dos documentos de estágio para que os alunos recebam feedback imediato e a coordenação reduza o trabalho manual de verificação?"*

**Pontos de Vista (POV):**

- **Lucas** precisa de **feedback claro e imediato** sobre seus documentos porque **não tem como saber se cometeu um erro sem aguardar dias pela resposta da coordenação**.
- **Carla** precisa de **um sistema que filtre os erros simples automaticamente** porque **gasta a maior parte do seu tempo corrigindo inconsistências básicas que poderiam ser identificadas automaticamente**.

---

#### 3.3. Ideação

**Brainstorming de ideias:**

1. Sistema de upload de documentos com validação automática de campos obrigatórios
2. Motor de regras baseado na Lei 11.788/08 e nas normas do IBMEC
3. Retorno automático com status (Aprovado / Reprovado / Pendente) e justificativas detalhadas
4. Histórico de submissões acessível pelo aluno
5. Painel para o coordenador acompanhar todas as solicitações em tempo real
6. Notificações automáticas ao aluno em cada mudança de status
7. Checklist dinâmica de documentos por tipo de estágio (obrigatório ou não obrigatório)

**Critérios de seleção:**

- Impacto direto na redução do tempo de validação
- Viabilidade técnica com Django e Python
- Alinhamento com os requisitos levantados no Brainstorm (BS01–BS15)

**Ideias selecionadas:**

1. **API de submissão e validação automática** — o aluno envia os dados do estágio em JSON, o sistema aplica as regras e retorna o resultado com justificativas
2. **Motor de regras configurável** — baseado na legislação e nas normas do IBMEC, verificando carga horária, documentos obrigatórios e conformidade do plano de atividades
3. **Histórico e status em tempo real** — o aluno pode acompanhar todas as suas submissões e o resultado de cada validação

---

#### 3.4. Prototipagem

**Descrição do Protótipo:**

Foi desenvolvido um protótipo de baixa fidelidade representando as principais telas do sistema: tela de login, formulário de submissão do estágio, tela de status da validação e histórico de submissões.

No backend, o protótipo consiste na definição das rotas da API:

| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/api/auth/login` | Autenticação do usuário |
| POST | `/api/estagios/` | Submissão de um novo estágio |
| GET | `/api/estagios/{id}/status` | Consulta do status da validação |
| GET | `/api/estagios/historico` | Histórico de submissões do aluno |

**Materiais Utilizados:**

- Figma para o protótipo de baixa fidelidade das telas
- PlantUML para modelagem do diagrama de classes e casos de uso
- Django e Python para o desenvolvimento do backend
- MkDocs para a documentação do projeto

**Testes Realizados:**

O protótipo foi apresentado à equipe para validação interna, verificando se os fluxos cobrem os casos de uso definidos e se as regras de negócio estão corretamente mapeadas.

---

#### 3.5. Teste

**Feedback:**

- O fluxo de submissão ficou claro e direto
- Identificou-se a necessidade de detalhar melhor as mensagens de erro retornadas pela API para que o aluno entenda exatamente o que precisa corrigir
- Sugestão de incluir uma checklist prévia para o aluno antes de submeter os documentos

**Ajustes Realizados:**

- Inclusão de mensagens de erro detalhadas nas respostas da API
- Definição de um campo `pendencias` no retorno da validação, listando item a item o que precisa ser corrigido

**Resultados Finais:**

A solução proposta automatiza as validações mais recorrentes, reduzindo o retrabalho da coordenação e fornecendo feedback imediato ao aluno. A arquitetura baseada em API permite integração futura com o sistema SIA do IBMEC.

---

### 4. Conclusão

**Resultados Obtidos:**

O processo de Design Thinking permitiu mapear com clareza o problema enfrentado pelos alunos e pela coordenação do IBMEC na gestão de estágios. A partir da empatia com os usuários, foi possível definir um problema central e propor uma solução tecnicamente viável e de alto impacto.

**Próximos Passos:**

- Desenvolver as rotas da API com Django
- Implementar o motor de regras baseado na Lei 11.788/08
- Integrar com banco de dados para persistência do histórico de validações
- Realizar testes com usuários reais (alunos e coordenadores)

**Aprendizados:**

- A validação manual é o principal gargalo do processo atual
- Feedback claro e imediato é o que os alunos mais precisam
- A automação deve complementar, não substituir, a análise final do orientador

---

### 5. Anexos

- [Pesquisa sobre Gestão de Estágio](pesquisa.md)
- [5W2H](5w2h.md)
- [Brainstorm](brainstorm.md)
- [Mapa Mental](mapa_mental.md)

---

## Versionamento

| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| 16/04/2026 | 1.0 | Criação do documento de Design Thinking | Gabriel Barreto, Guilherme Braz, Ísis Tavares, Mariana Faria e Matheus Alvarenga |
